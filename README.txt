This project was aimed at automating the process of transposing RPS Calculator v6.2 renewable portfolios to RESOLVE
inputs. The project contains two scripts, Config.py and Portfolio_Mapper.py, and requires a CSV represent the "exported"
results from the RPS Calculator v6.2.

In short, with the except of the small changes needed to be made to the raw CSV (see INPUT CSVs below), this script
should pretty much work out of the box. It required a lot of data inputting but the names of RESOLVE technologies and
RPS Calculator resources don't change often enough for there to be much alteration at this point.

%%%%%%%%%%%% INPUT CSVs %%%%%%%%%%%%
All CSVs in this project that end with the word "Raw.csv" represent appropriate input CSVs. These are the CSVs created
when one clicks "Export results" on the RPS Calculator v6.2, with 3 minor changes:
    1) One should search for all and remove all commas in the exported results file.
    2) In the raw exported results, there is a linebreak in cell Y1 -- this needs to be removed.
    3) This isn't likely to change without an update to the RPS Calculator, but one should make sure that the indices
       found in Config.py that map data to column numbers is correct.

%%%%%%%%%%%% PYTHON SCRIPTS %%%%%%%%%%%%
Config.py
    This script holds much of the data required to run Portfolio_Mapper, the main script of the project.
    -top_unmapped_to_show gives the number of largest unmapped RPS Calculator resources to print.
    -RESOLVE_years lists the years that will be used in the RESOLVE instance
    -RESOLVE_technologies lists the types of RESOLVE technologies
    -RESOLVE_locations lists the zones that RESOLVE is modeling
    -RESOLVE_resources is a dictionary:
        -each key should be a RESOLVE resource to be modeled, and the corresponding value should be the zone where the
        resource is located
    -RPS_to_RESOLVE_technologies maps RPS Calculator names for technologies to RESOLVE names
    -RPS_to_RESOLVE_CREZ_conversions is the crucial dictionary for Portfolio_Mapper.py:
        -each key is a 3-element tuple consistent of the CREZ, the technology type, and the location
        -the corresponding value is a list of RESOLVE resources, with each element representing the RPS Calculator
        "categories":
            1) Existing resource: These are renewable resources currently online
            2) Commercial resource:
            3) Recontracted resource: These are renewable resources that the RPS calculator has decided to recontract
               after the in-place contract expires
            4) Generic resource: these are generic resources that the RPS calculator decides to build to meet RPS needs.

Portfolio_Mapper.py
    The following is pseudo-code for the Portfolio_Mapper.py script:

    For every row in the RPS Calculator raw data:
        -Take the following from the row:
            -Project name
            -Category (1-4)
            -State
            -CREZ
            -Technology
            -Start date
            -End date
            -Located In CAISO boolean
            -Contracted To CAISO boolean
            -Capacity
            -Energy
            -Degradation
            -Risk adjustment

        -If the technology is in our list of RPS technologies & the resource is Contracted To CAISO:
            -For every RESOLVE year:
                -Scale down the row energy by Risk Adjustment, Degradation and % of year resource is online for
