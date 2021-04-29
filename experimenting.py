#import modules - CSV MUST!

import csv

#dev to read csv (r)
def read_data ():
    data = []

    with open('emissions.csv', 'r') as emissions_csv: #make sure 'emissions.csv' is in same folder as this file!
        spreadsheet = csv.DictReader(emissions_csv)
        for row in spreadsheet:
            data.append(row)

    return data


#dev to run
def total_run ():
    data = read_data() #becomes tag for previous def

    ghg = [] #creates blank list to add csv data - gfg
    co2 = [] #creates blank list to add csv data - co2

    for row in data:
        greenhousegas = float(row['ghg']) #float not int because of decimal
        ghg.append(greenhousegas) #append ghg emissions csv data into list

        carbondioxide = float(row['co2'])
        co2.append(carbondioxide) #append co2 emissions csv data into list

    # 600 entries = len(ghg) and len(co2)
    # print(ghg)
    # print(co2)

    total_ghg = sum(ghg) #sum of ghg data
    round_total_ghg = round((total_ghg), 2)
    print('Total greenhouse gas emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_total_ghg)) #measurements?

    total_co2 = sum(co2) #sum of ghg data
    round_total_co2 = round((total_co2), 2)
    print('Total carbon dioxide emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_total_co2)) #measurements?

    avr_ghg = sum(ghg) / len(ghg) #sum of ghg data
    round_avr_ghg = round((avr_ghg), 2)
    print('Average greenhouse gas emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_avr_ghg)) #measurements?

    avr_co2 = sum(co2) / len(co2) #sum of ghg data
    round_avr_co2 = round((avr_co2), 2)
    print('Average carbon dioxide emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_avr_co2)) #measurements?

    max_ghg = max(ghg)  # sum of ghg data
    round_max_ghg = round((max_ghg), 2)
    print('Max greenhouse gas emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_max_ghg))  # measurements?

    max_co2 = max(co2)  # sum of ghg data
    round_max_co2 = round((max_co2), 2)
    print('Max carbon dioxide emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_max_co2))  # measurements?

total_run()

from csv import DictReader

with open('emissions.csv', 'r') as read_object:
    dict_reader = DictReader(read_object)
    emissions_dict = list(dict_reader)
    # print(emissions_dict)
#
def max_run():
    max_ghg = max(total_run(ghg))   # max num in ghg data
    print(max_ghg)

    if max_ghg in emissions_dict:
        industry_max = ['industry']
    return industry_max

    max_ghg = max(total_run(ghg))  # sum of ghg data
    round_max_ghg = round((max_ghg), 2)
    print('Max greenhouse gas emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_max_ghg))  # measurements?

    max_co2 = max(co2)  # sum of ghg data
    round_max_co2 = round((max_co2), 2)
    print('Max carbon dioxide emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_max_co2))  # measurements?

max_run()