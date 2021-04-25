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
def run ():
    data = read_data() #becomes tag for previous def

    ghg = [] #creates blank list to add csv data - gfg
    co2 = [] #creates blank list to add csv data - co2

    for row in data:
        greenhousegas = float(row['ghg']) #float not int because of decimal
        ghg.append(greenhousegas) #append ghg emissions csv data into list

        carbondioxide = float(row['co2'])
        co2.append(carbondioxide) #append co2 emissions csv data into list

    total = sum(ghg) #sum of ghg data
    print('Total Greenhouse gas emissions intensity by industry, 1990 to 2018 and (provisional) 2019: {}'.format(total)) #measurements?

    total = sum(co2) #sum of ghg data
    print('Total Carbon dioxide emissions intensity by industry, 1990 to 2018 and (provisional) 2019: {}'.format(total)) #measurements?

run()

#code output Total ghg: 536.0199999999992  Total co2: 321.2199999999991