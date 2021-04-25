#import modules - CSV MUST!

import csv

#dev to read csv (r)
def read_data ():
    data = []

    with open('sales.csv', 'r') as sales_csv: #make sure 'sales.csv' is in same folder as this file!
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data


#dev to run
def run ():
    data = read_data() #becomes tag for previous def

    sales = [] #creates blank list to add csv data
    for row in data:
        sale = int(row['sales'])
        sales.append(sale) #append sales csv data into list

    total = sum(sales) #sum of sales data
    print('Total sales: {}'.format(total))

run()

#code output = 'Total sales: 45542'


