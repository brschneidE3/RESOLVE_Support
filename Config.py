__author__ = 'brendan'

RPS_Calc_category_index = 1
RPS_Calc_project_index = 3
RPS_Calc_state_index = 4
RPS_Calc_CREZ_index = 6
RPS_Calc_tech_index = 10
RPS_Calc_start_index = 13
RPS_Calc_end_index = 14
RPS_Calc_CAISO_loc_bool_index = 17
RPS_Calc_nonCAISO_contracted_bool_index = 24
RPS_Calc_capacity_index = 25
RPS_Calc_energy_index = 26
RPS_Calc_degrade_index = 32
RPS_Calc_riskadjust_index = 33


top_unmapped_to_show = 10
RESOLVE_years = [2016, 2020, 2025, 2030]
RESOLVE_technologies = ['Conventional', 'Battery', 'Pumped_Storage', 'Hydro', 'Biomass', 'Geothermal', 'Small_Hydro',
                        'Solar', 'Wind', 'Customer_PV']
RESOLVE_locations = ['CAISO', 'NW', 'SW', 'LADWP']

# Resource name as key, location as value
RESOLVE_resources = {
    'CAISO_CHP' : 'CAISO',
    'CAISO_Nuclear' : 'CAISO',
    'CAISO_CCGT1' : 'CAISO',
    'CAISO_CCGT2' : 'CAISO',
    'CAISO_Peaker1' : 'CAISO',
    'CAISO_Peaker2' : 'CAISO',
    'CAISO_Advanced_CCGT' : 'CAISO',
    'CAISO_Aero_CT' : 'CAISO',
    'CAISO_Reciprocating_Engine' : 'CAISO',
    'CAISO_ST' : 'CAISO',
    'CAISO_CCGT_Retrofit' : 'CAISO',
    'CAISO_Conventional_DR' : 'CAISO',
    'CAISO_Storage_Mandate' : 'CAISO',
    'CAISO_New_Flow_Battery' : 'CAISO',
    'CAISO_Existing_Pumped_Storage' : 'CAISO',
    'CAISO_New_Li_Battery' : 'CAISO',
    'CAISO_New_Pumped_Storage' : 'CAISO',
    'CAISO_Hydro' : 'CAISO',
    'Small_Hydro' : 'CAISO',
    'Contracted_InState_Biomass' : 'CAISO',
    'Contracted_InState_Geothermal' : 'CAISO',
    'Contracted_InState_Small_Hydro' : 'CAISO',
    'Contracted_InState_Solar' : 'CAISO',
    'Contracted_InState_Wind' : 'CAISO',
    'Customer_PV' : 'CAISO',
    'Distributed_Solar' : 'CAISO',
    'Distributed_Wind' : 'CAISO',
    'InState_Biomass' : 'CAISO',

    'Contracted_NW_Geothermal' : 'NW',
    'Contracted_NW_Wind' : 'NW',
    'Contracted_SW_Geothermal' : 'SW',
    'Contracted_SW_Solar' : 'SW',
    'Contracted_SW_Wind': 'SW',
    'Contracted_NW_Biomass' : 'NW',
    'Utah_Wind' : 'NW',
    'Wyoming_Wind': 'NW',
    'Southern_Nevada_Northwest_Arizona_Solar' : 'SW',


    'Baja_California_Wind': 'CAISO',
    'Central_Valley_North_Los_Banos_Solar' : 'CAISO',
    'Central_Valley_North_Los_Banos_Wind' : 'CAISO',
    'Greater_Carrizo_Solar' : 'CAISO',
    'Greater_Imperial_Solar' : 'CAISO',
    'Greater_Imperial_Geothermal': 'CAISO',
    'Greater_Imperial_Wind' : 'CAISO',
    'Kramer_Inyokern_Solar' : 'CAISO',
    'Kramer_Inyokern_Wind': 'CAISO',
    'Mountain_Pass_El_Dorado_Solar' : 'CAISO',
    'Northern_California_Geothermal' : 'CAISO',
    'Northern_California_Solar' : 'CAISO',
    'Northern_California_Wind': 'CAISO',
    'Pacific_Northwest_Wind': 'CAISO',
    'Solano_Wind' : 'CAISO',
    'Solano_Solar' : 'CAISO',
    'Southern_California_Desert_Solar' : 'CAISO',
    'Riverside_East_Palm_Springs_Solar' : 'CAISO',
    'Riverside_East_Palm_Springs_Wind' : 'CAISO',
    'Tehachapi_Solar' : 'CAISO',
    'Tehachapi_Wind': 'CAISO',
    'Westlands_Solar' : 'CAISO'
}

#RPS tech names are keys, RESOLVE tech names are values
RPS_to_RESOLVE_technologies = {
    'Biogas' : 'Biomass', #FIXME,
    'Biomass' : 'Biomass',
    'Geothermal': 'Geothermal',
    'Hydro': 'Hydro',
    'Solar PV': 'Solar', #FIXME: Solar or Customer_PV?
    'Solar Thermal': 'Solar', #FIXME
    'Wind': 'Wind',
    'Various' : None #FIXME
}


#RPS CREZ and technology names are keys, RESOLVE CREZ names are values, indexed by RPS calculator "category"
RPS_to_RESOLVE_CREZ_conversions = {

    #Clear mappings
    ('Barstow',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Kramer_Inyokern_Solar'],
    ('Baja',	'Wind', 'BJ') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Baja_California_Wind'],
    ('Carrizo North',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Greater_Carrizo_Solar'],
    ('Carrizo South',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Greater_Carrizo_Solar'],
    ('Imperial East',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Greater_Imperial_Wind'],
    ('Imperial',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Greater_Imperial_Solar'],
    ('Imperial',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Greater_Imperial_Wind'],
    ('Inyokern',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Kramer_Inyokern_Solar'],
    ('Iron Mountain',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Southern_California_Desert_Solar'],
    ('Kramer',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Kramer_Inyokern_Solar'],
    ('Kramer',	'Solar Thermal', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Kramer_Inyokern_Solar'],
    ('Los Banos',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Central_Valley_North_Los_Banos_Solar'],
    ('Mountain Pass',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Mountain_Pass_El_Dorado_Solar'],
    ('Mountain Pass',	'Solar Thermal', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Mountain_Pass_El_Dorado_Solar'],
    ('Palm Springs',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Riverside_East_Palm_Springs_Solar'],
    ('Palm Springs',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Riverside_East_Palm_Springs_Wind'],
    ('Riverside County (Partial)',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Riverside_East_Palm_Springs_Solar'],
    ('Riverside East',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Riverside_East_Palm_Springs_Solar'],
    ('Riverside East',	'Solar Thermal', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Riverside_East_Palm_Springs_Solar'],
    ('Riverside East',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Riverside_East_Palm_Springs_Wind'],
    ('Round Mountain - B',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Northern_California_Solar'],
    ('Sacramento River Valley',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Northern_California_Solar'],
    ('Sacramento River',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Northern_California_Solar'],
    ('San Bernardino - Baker',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Southern_California_Desert_Solar'],
    ('San Bernardino - Lucerne',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Kramer_Inyokern_Solar'],
    ('San Diego North Central',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Greater_Imperial_Solar'],
    ('San Diego South',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Greater_Imperial_Solar'],
    ('San Diego South',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Greater_Imperial_Wind'],
    ('Santa Barbara',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Greater_Carrizo_Solar'],
    ('Solano',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Solano_Solar'],
    ('Solano',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Solano_Wind'],
    ('Tehachapi',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Tehachapi_Solar'],
    ('Twentynine Palms',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Southern_California_Desert_Solar'],
    ('Victorville',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Kramer_Inyokern_Solar'],
    ('Victorville',	'Solar Thermal', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Kramer_Inyokern_Solar'],
    ('Westlands',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Westlands_Solar'],


    ('AB_EA', 'Wind', 'AB') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('AB_EC', 'Wind', 'AB') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('AZ_WE', 'Solar PV', 'AZ') : ['Contracted_SW_Solar', 'Contracted_SW_Solar', 'Contracted_SW_Solar', 'Contracted_SW_Solar'],
    ('Baja',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Baja_California_Wind'],

    ('ID_EA', 'Wind', 'ID') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('Los Angeles County (Partial)',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'], 

    ('MT_NW','Wind', 'MT') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('NM_EA', 'Wind', 'NM'): ['Contracted_SW_Wind', 'Contracted_SW_Wind', 'Contracted_SW_Wind', 'Greater_Imperial_Wind'],
    ('NV_NO', 'Geothermal', 'NV') : ['Contracted_SW_Geothermal', 'Contracted_SW_Geothermal', 'Contracted_SW_Geothermal', 'Contracted_SW_Geothermal'],
    ('NV_SW', 'Solar PV', 'NV') : ['Contracted_SW_Solar', 'Contracted_SW_Solar', 'Contracted_SW_Solar', 'Southern_Nevada_Northwest_Arizona_Solar'],
    ('WA_SO', 'Wind', 'WA') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('WA_SO', 'Wind', 'OR') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('WY_EC', 'Wind', 'WY') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Wyoming_Wind'],
    ('WY_EA', 'Wind', 'WY') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Wyoming_Wind'],

    ('Amador County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Calaveras County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Central Valley North',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('El Dorado County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Humboldt County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Inyo County (Partial)',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Inyokern',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Lassen North',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Lassen South',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Los Banos',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Mendocino County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Mono County (Partial)',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Nevada County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Orange County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Owens Valley',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Palm Springs',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Placer County (Partial)',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Plumas County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Round Mountain - B',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Sacramento River',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('San Bernardino - Lucerne',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('San Diego North Central',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Santa Barbara',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Santa Clara County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Sierra County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Solano',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Sonoma County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Tehachapi',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Trinity County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Tuolumne County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Ventura County (Partial)',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Westlands',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],
    ('Yuba County',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],

    ('Imperial',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Greater_Imperial_Geothermal'],
    ('Imperial North',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Greater_Imperial_Geothermal'],
    ('Imperial South',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Greater_Imperial_Geothermal'],
    ('Lassen North',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Northern_California_Geothermal'],
    ('Los Banos',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Central_Valley_North_Los_Banos_Wind'],
    ('Round Mountain',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Northern_California_Wind'],
    ('Sacramento River',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Northern_California_Wind'],
    ('San Diego County (Partial)',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Greater_Imperial_Solar'],
    ('Sonoma County',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Northern_California_Geothermal'],
    ('Tehachapi',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Tehachapi_Wind'],
    ('Victorville',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Kramer_Inyokern_Wind'],

    ('n/a',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('n/a',	'Biogas', 'WA') : ['Contracted_NW_Biomass', 'Contracted_NW_Biomass', 'Contracted_NW_Biomass', 'Contracted_NW_Biomass'],
    ('n/a',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('n/a',	'Biomass', 'WA') : ['Contracted_NW_Biomass', 'Contracted_NW_Biomass', 'Contracted_NW_Biomass', 'Contracted_NW_Biomass'],
    ('n/a',	'Geothermal', 'UT') : ['Contracted_SW_Geothermal', 'Contracted_SW_Geothermal', 'Contracted_SW_Geothermal', 'Contracted_SW_Geothermal'],
    ('n/a',	'Wind', 'WA') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('n/a',	'Geothermal', 'NV') : ['Contracted_SW_Geothermal', 'Contracted_SW_Geothermal', 'Contracted_SW_Geothermal', 'Contracted_SW_Geothermal'],
    ('n/a',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Small_Hydro'],

    ('n/a',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar'],
    ('n/a',	'Solar PV', 'NV') : ['Contracted_SW_Solar', 'Contracted_SW_Solar', 'Contracted_SW_Solar', 'Southern_Nevada_Northwest_Arizona_Solar'],
    ('n/a',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind'],
    ('n/a',	'Wind', 'ID') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('n/a',	'Wind', 'OR') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Pacific_Northwest_Wind'],
    ('n/a',	'Wind', 'WY') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Wyoming_Wind'],
    ('n/a',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal'],
    ('N/A', 'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar'],
    ('Unknown',	'Hydro', 'CA') : ['Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro', 'Contracted_InState_Small_Hydro'],

    ('Cuyama',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Fairmont',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Humboldt County',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Lassen North',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Los Angeles County (Partial)',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Los Banos',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Marin County',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Monterey County (Partial)',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Orange County',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Palm Springs',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Placer County (Partial)',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Plumas County',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Riverside County (Partial)',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Round Mountain - B',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Sacramento River',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Sacramento River',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('San Bernardino - Lucerne',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('San Diego North Central',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('San Diego South',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Santa Barbara',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Santa Clara County',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Santa Cruz County',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Solano',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Solano',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Tehachapi',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Tuolumne County',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Ventura County (Partial)',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Westlands',	'Biogas', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('Westlands',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],
    ('NonCREZ',	'Biomass', 'CA') : ['Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'Contracted_InState_Biomass', 'InState_Biomass'],

    #TODO: Ignore "VARIOUS" technology
    ('N/A',	'Various', 'CA') : [None, None, None, None],
    ('Unknown',	'Various', 'CA') : [None, None, None, None],
    ('Imperial North',	'Various', 'CA') : [None, None, None, None],

    #TODO: Ignore WA hydro
    ('n/a',	'Hydro', 'WA') : [None, None, None, None],


    ('n/a',	'Biogas', 'UT') : ['Contracted_NW_Biomass', 'Contracted_NW_Biomass', 'Contracted_NW_Biomass', 'Contracted_NW_Biomass'],
    ('n/a',	'Wind', 'UT') : ['Contracted_NW_Wind', 'Contracted_NW_Wind', 'Contracted_NW_Wind', 'Utah_Wind'],


    ('Fairmont',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Tehachapi_Solar'],
    ('Los Angeles County (Partial)',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Tehachapi_Solar'],
    ('Nevada C',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Southern_California_Desert_Solar'],
    ('Nevada C',	'Solar PV', 'NV') : ['Contracted_SW_Solar', 'Contracted_SW_Solar', 'Contracted_SW_Solar', 'Southern_Nevada_Northwest_Arizona_Solar'],
    ('San Benito County',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Central_Valley_North_Los_Banos_Solar'],
    ('Orange County', 'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Tehachapi_Solar'],
    ('Placer County (Partial)',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Northern_California_Solar'],
    ('San Francisco County',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Northern_California_Solar'],
    ('Sonoma County',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', 'Solano_Solar'],


    ('Inyokern',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Northern_California_Geothermal'],
    ('Nevada C',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Greater_Imperial_Geothermal'],
    ('Nevada C',	'Geothermal', 'NV') : ['Contracted_SW_Geothermal', 'Contracted_SW_Geothermal', 'Contracted_SW_Geothermal', 'Contracted_SW_Geothermal'],
    ('Mono County (Partial)',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Northern_California_Geothermal'],
    ('Owens Valley',	'Geothermal', 'CA') : ['Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Contracted_InState_Geothermal', 'Greater_Imperial_Geothermal'],

    ('Barstow',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Kramer_Inyokern_Wind'],
    ('Distributed',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', 'Distributed_Wind'],

    ('Tuolumne County',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', None], #FIXME
    ('Ventura County (Partial)',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', None], #FIXME
    ('Yuba County',	'Solar PV', 'CA') : ['Contracted_InState_Solar', 'Contracted_InState_Solar', 'Contracted_InState_Solar', None], #FIXME
    ('San Bernardino - Lucerne',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', None], #FIXME: Southern_California_Desert
    ('Santa Clara County',	'Wind', 'CA') : ['Contracted_InState_Wind', 'Contracted_InState_Wind', 'Contracted_InState_Wind', None], #FIXME
}