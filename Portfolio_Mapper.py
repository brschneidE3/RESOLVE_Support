__author__ = 'brendan'

# This script takes a result of the RPS calculator and translates it into a set of resources required for RESOLVE

import beesh
import os
import Config
import datetime
import operator

wd = os.getcwd()

# Note:
# all commas must be removed
# linebreak in header of column Y must be removed
# indices much match those in Config
input_filename = 'Out_of_State_UPDATE_LL Raw'
inputfile_path = r'\%s.csv' % input_filename

outputfile_path = r'\%s.csv' % (input_filename[:-4]+' Results')
# outputfile_path = r'\DEBUG_Results.csv'


# Date rounding
# Risk adjustment
# Degradation


# RPS Calc data read in as RowData object
RSPCalc_data_list = beesh.csv_to_list(os.getcwd(), inputfile_path, 1, 1)
RPS_Calc_data = {}
RPS_Capacity = {yr: 0 for yr in Config.RESOLVE_years}
RPS_Energy = {yr: 0 for yr in Config.RESOLVE_years}
RPS_Biogas = {yr: 0 for yr in Config.RESOLVE_years}
RPS_Biomass = {yr: 0 for yr in Config.RESOLVE_years}

capacities = []
for row in RSPCalc_data_list[1:]:

    RowData = beesh.EmptyClass()

    try:
        # hardcoded data cleaning
        start_date = datetime.date(1900, 1, 1) if row[Config.RPS_Calc_start_index] in ['1/0/1900', '0'] else \
            datetime.date(
            int(row[Config.RPS_Calc_start_index].rsplit('/')[2]),
            int(row[Config.RPS_Calc_start_index].rsplit('/')[0]),
            int(row[Config.RPS_Calc_start_index].rsplit('/')[1]),
            )
        end_date = datetime.date(1900, 1, 1) if row[Config.RPS_Calc_end_index] in ['1/0/1900', '0'] else \
            datetime.date(
            int(row[Config.RPS_Calc_end_index].rsplit('/')[2]),
            int(row[Config.RPS_Calc_end_index].rsplit('/')[0]),
            int(row[Config.RPS_Calc_end_index].rsplit('/')[1]),
        )

        if end_date.year >= min(Config.RESOLVE_years) and start_date.year <= max(Config.RESOLVE_years)+1:
            RowData.project_name = row[Config.RPS_Calc_project_index]
            RowData.category = int(row[Config.RPS_Calc_category_index])  # 1: Existing 2: Comm 3: Recontract 4: Generic
            RowData.state = row[Config.RPS_Calc_state_index]
            RowData.CREZ = row[Config.RPS_Calc_CREZ_index]
            RowData.technology = row[Config.RPS_Calc_tech_index]
            RowData.start_date = start_date
            RowData.end_date = end_date
            RowData.Loc_In_CAISO = True if row[Config.RPS_Calc_CAISO_loc_bool_index] == '1' else False
            RowData.Contr_To_CAISO = True if row[Config.RPS_Calc_nonCAISO_contracted_bool_index] == '0' else False
            RowData.capacity = float(row[Config.RPS_Calc_capacity_index])
            RowData.energy = float(row[Config.RPS_Calc_energy_index])
            RowData.degradation = float(row[Config.RPS_Calc_degrade_index])
            RowData.risk_adjustment = float(row[Config.RPS_Calc_riskadjust_index])

            if RowData.technology in ['Biomass', 'Biogas', 'Geothermal', 'Hydro', 'Solar PV', 'Solar Thermal', 'Wind'] and RowData.Contr_To_CAISO:

                RowData.Mapped = False #Boolean signifying whether or not this RPS Calc resource has been mapped to the RESOLVE portfolio

                RPS_Calc_data[int(row[0])] = RowData

                #TODO: Update degradation, risk and % of year

                RowData.Final_Energies = {year : None for year in Config.RESOLVE_years}
                RowData.Final_Capacities = {year: None for year in Config.RESOLVE_years}
                for year in Config.RESOLVE_years:

                    scaled_down_energy = RowData.energy*(RowData.risk_adjustment)*((1 - RowData.degradation)**max(year - RowData.start_date.year,0))
                    end_date_in_year = min(end_date,datetime.date(year+1,1,1))
                    start_date_in_year = max(start_date,datetime.date(year,1,1))
                    days_active_in_year = max((end_date_in_year - start_date_in_year).days, 0)
                    days_in_year = (datetime.date(year+1,1,1) - datetime.date(year,1,1)).days
                    pct_of_year_online = float(days_active_in_year)/float(days_in_year)

                    final_energy = scaled_down_energy*pct_of_year_online
                    RowData.Final_Energies[year] = final_energy
                    RPS_Energy[year] += final_energy

                    if RowData.start_date <= datetime.date(year,12,31) and RowData.end_date > datetime.date(year,12,31):
                        final_capacity = RowData.capacity*RowData.risk_adjustment
                    else:
                        final_capacity = 0
                    RowData.Final_Capacities[year] = final_capacity
                    RPS_Capacity[year] += final_capacity


                if end_date <= start_date:
                    print "End date precedes start date for:"
                    print row
                    exit()

    except:
        print 'Error with following row:'
        print row
        print row[Config.RPS_Calc_end_index].rsplit('/')
        print row[Config.RPS_Calc_end_index].rsplit('/')
        exit()


#Create output_portfolio dictionary where RESOLVE inputs will be populated
output_portfolio = {}
energy_portfolio = {}
for resource in Config.RESOLVE_resources.keys():
    location = Config.RESOLVE_resources[resource]

    for technology in Config.RESOLVE_technologies:
        for period in Config.RESOLVE_years:

            #CREATE ROW FOR RESOLVE INPUT FILE
            #output_portfolio[(resource, technology, location, 'CAISO', period)] = 0
            #energy_portfolio[(resource, technology, location, 'CAISO', period)] = 0

            #ITERATE THROUGH ALL RPS CALC DATA AND ADD CAPACITY TO RESOLVE INPUT FILE ROW
            for RPS_Calc_resource in RPS_Calc_data.values():

                #FILTER BY CONTRACT DATES
                if RPS_Calc_resource.start_date <= datetime.date(period,12,31):
                    if RPS_Calc_resource.end_date >= datetime.date(period,1,1):

                        #FILTER BY TECHNOLOGY
                        RESOLVE_TECHNOLOGY_NAME = Config.RPS_to_RESOLVE_technologies[RPS_Calc_resource.technology]
                        #print 'TECHNOLOGY MAPPING:'
                        #print '%s mapped to %s'%(RPS_Calc_resource.technology,RESOLVE_TECHNOLOGY_NAME)
                        if RESOLVE_TECHNOLOGY_NAME == technology:

                            #FILTER BY RESOURCE
                            RESOLVE_RESOURCE_NAME = Config.RPS_to_RESOLVE_CREZ_conversions[(RPS_Calc_resource.CREZ, RPS_Calc_resource.technology, RPS_Calc_resource.state)][RPS_Calc_resource.category-1]

                            if RESOLVE_RESOURCE_NAME == resource:
                                try:
                                    output_portfolio[(resource, technology, location, 'CAISO', period)] += RPS_Calc_resource.Final_Capacities[period]
                                    energy_portfolio[(resource, technology, location, 'CAISO', period)] += RPS_Calc_resource.Final_Energies[period]
                                except KeyError:
                                    output_portfolio[(resource, technology, location, 'CAISO', period)] = RPS_Calc_resource.Final_Capacities[period]
                                    energy_portfolio[(resource, technology, location, 'CAISO', period)] = RPS_Calc_resource.Final_Energies[period]
                                RPS_Calc_resource.Mapped = True


Unmapped_RPS_data = {}
for RPS_Calc_resource in RPS_Calc_data.values():
    if RPS_Calc_resource.Mapped == False:
        Unmapped_RPS_data[RPS_Calc_resource] = (RPS_Calc_resource.capacity, RPS_Calc_resource.energy)

###################
#PRINT SUMMARY INFO
###################
CapacityFound = {yr : 0 for yr in Config.RESOLVE_years}
EnergyFound = {yr : 0 for yr in Config.RESOLVE_years}

# for i in range(len(output_portfolio.values())):
#     if output_portfolio.values()[i] > 0:
#         year = output_portfolio.keys()[i][4]
#         CapacityFound[year] += output_portfolio.values()[i]

for i in range(len(output_portfolio.keys())):
    key = output_portfolio.keys()[i]
    capacity = output_portfolio[key]
    energy = energy_portfolio[key]
    if capacity > 0:
        year = key[4]
        CapacityFound[year] += capacity
        EnergyFound[year] += energy

Mapped = []
for year in CapacityFound:
    Mapped.append([
        year,int(CapacityFound[year]),int(RPS_Capacity[year]),str(100.*CapacityFound[year]/RPS_Capacity[year])[:4],
                   int(EnergyFound[year]),int(RPS_Energy[year]),str(100.*EnergyFound[year]/RPS_Energy[year])[:4]
                   ])
Mapped.append(['TOTAL',
               int(sum(CapacityFound.values())),int(sum(RPS_Capacity.values())),str(100.*sum(CapacityFound.values())/sum(RPS_Capacity.values()))[:4],
               int(sum(EnergyFound.values())),int(sum(RPS_Energy.values())),str(100.*sum(EnergyFound.values())/sum(RPS_Energy.values()))[:4]
               ])
print 'DATA SUMMARY:'
beesh.PrintTabularResults(['','Capacity Mapped (MW)', 'RPS Calc Capacity (MW)', '% Mapped','Energy Mapped (GWh)','RPS Calc Energy (GWh)', '% Mapped'],Mapped)

Sorted_Unmapped_RPS_Data = sorted(Unmapped_RPS_data.items(), key=operator.itemgetter(1))[::-1]
top_unmapped_to_show = Config.top_unmapped_to_show if Config.top_unmapped_to_show <= len(Sorted_Unmapped_RPS_Data) else len(Sorted_Unmapped_RPS_Data)
print '\n', "TOP %s UNMAPPED CONTRACTS:"%top_unmapped_to_show
Top_Unmapped = []
for unmapped_resource, capacity in Sorted_Unmapped_RPS_Data[:top_unmapped_to_show]:
    Top_Unmapped.append([unmapped_resource.project_name, unmapped_resource.CREZ, unmapped_resource.state, unmapped_resource.technology, unmapped_resource.capacity, unmapped_resource.energy, unmapped_resource.start_date, unmapped_resource.end_date])
beesh.PrintTabularResults(['Project Name', 'CREZ', 'State', 'Technology', 'Capacity', 'Energy', 'Start Date', 'End Date'],Top_Unmapped)

beesh.list_to_csv(wd + outputfile_path,
                  [['resource', 'technology', 'location', 'contract', 'period', 'planned_installed_capacity', 'energy', 'capacity factor']] +
                    [  list(key) + [output_portfolio[key], energy_portfolio[key], energy_portfolio[key]*1000./(output_portfolio[key]*8760.)] for key in output_portfolio.keys()])

missing_resources = []
for value_list in Config.RPS_to_RESOLVE_CREZ_conversions.values():
    for value in value_list:
        if value not in Config.RESOLVE_resources and value not in missing_resources:
            missing_resources.append(value)
print '\n', "The following are missing from CONFIG.RESOLVE_resources: "
for resource in missing_resources:
    print resource

#DONE: 1) Read in RPS Calc portfolio
#DONE: 2) Construct what you can given the mapping keys that are filled out
#DONE: 3) Compare % of MW in actual RPS calculator portfolio
#DONE 4) Try adding the todo category resources and repeat (3)
#TODO 5) Sort out RPS calculator "Category" functionality by making RPS_to_RESOLVE_CREZ_conversions map to a list of RESOLVE CREZ's, indexed by category
    #TODO: e.g. (RPS RESOURCE, RPS TECHNOLOGY) : [ RESOLVE RESOURCE IF CATEGORY = 1, .... , RESOLVE RESOURCE IF CATEGORY = 4 ]
    #TODO: ...OR...
    #TODO: (RPS RESOURCE, RPS TECHNOLOGY, RPS CATEGORY) : RESOLVE RESOURCE
#TODO 6) Talk to Ana (and Nick)