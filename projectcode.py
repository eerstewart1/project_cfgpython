import random
import requests
import operator
import sys
import time
import csv
from csv import DictReader

#slow print
def s_print(str):
    for letter in str + '\n':
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)

def read_data():

    data = []

    with open('emissions.csv', 'r') as read_object:
        dict_reader = DictReader(read_object)
        emissions_dict = list(dict_reader)
        for row in emissions_dict:
            data.append(row)
        # print(emissions_dict) #print dictionary with labels

    return data #data from csv put into dictionary

def interface ():
    s_print('Welcome! This is our Python project on CSV spreadsheet analysis.')
    s_print('Our topic is *Greenhouse Gas and CO2 Emissions Intensity by Industry* from the Office of National Statistics.')
    s_print('Our CSV contains greenhouse gas (GHG) and carbon dioxide (CO2) emissions output per unit of economic output.')
    s_print('Different industries, from retail to health care, were studied between 1990 to 2018, and 2019 provisionally.')
    s_print('What would you like to know about Atmospheric emissions?')

interface()

def options ():
    print('1. Total GHG emissions per unit of economic output across all industries between 1990 and 2019.')
    print('2. Total CO2 emissions per unit of economic output across all industries between 1990 and 2019.')
    print('3. Average GHG emissions per unit of economic output across all industries between 1990 and 2019.')
    print('4. Average CO2 emissions per unit of economic output across all industries between 1990 and 2019.')
    print('5. Maximum GHG emissions per unit of economic output across all industries between 1990 and 2019.')
    print('6. Maximum CO2 emissions per unit of economic output across all industries between 1990 and 2019.')
    print('7. Minimum GHG emissions per unit of economic output across all industries between 1990 and 2019.')
    print('8. Minimum CO2 emissions per unit of economic output across all industries between 1990 and 2019.')

options()

def options_input():
    print('Please input 1 to 8. If you wish to exit, input Bye. ')
    option = input()

    if option == '1':
        def total_ghg_run():
            data = read_data()  # becomes tag for previous def
            ghg_total_list = []  # creates blank list to add csv data - gfg

            for row in data:
                greenhousegas = float(row['ghg'])  # float not int because of decimal
                ghg_total_list.append(greenhousegas)  # append ghg emissions csv data into list

            total_ghg = sum(ghg_total_list)  # sum of ghg data
            round_total_ghg = round((total_ghg), 2)
            s_print('Total GHG emissions: {} per 600 recorded economic units across all industries between 1990 to 2019.'.format(round_total_ghg))

        total_ghg_run()
        options_input()

    elif option == '2':
        def total_co2_run():
            data = read_data()  # becomes tag for previous def
            co2_total_list = []  # creates blank list to add csv data - gfg

            for row in data:
                carbondioxide = float(row['co2'])
                co2_total_list.append(carbondioxide)  # append co2 emissions csv data into list

            total_co2 = sum(co2_total_list)  # sum of ghg data
            round_total_co2 = round((total_co2), 2)
            s_print('Total CO2 emissions: {} per 600 recorded economic units across all industries between 1990 to 2019.'.format(round_total_co2))

        total_co2_run()
        options_input()

    elif option == '3':
        def avr_ghg_run():
            data = read_data()  # becomes tag for previous def
            ghg_avr_list = []  # creates blank list to add csv data - gfg

            for row in data:
                greenhousegas = float(row['co2'])
                ghg_avr_list.append(greenhousegas)  # append co2 emissions csv data into list

            avr_ghg = sum(ghg_avr_list) / len(ghg_avr_list)  # sum of ghg data
            round_avr_ghg = round((avr_ghg), 2)
            print('Average greenhouse gas emissions: {} per economic unit'.format(round_avr_ghg))

        avr_ghg_run()
        options_input()

    elif option == '4':
        def avr_co2_run():
            data = read_data()  # becomes tag for previous def
            co2_avr_list = []  # creates blank list to add csv data - gfg

            for row in data:
                greenhousegas = float(row['co2'])
                ghg_co2_list.append(greenhousegas)  # append co2 emissions csv data into list

            avr_co2 = sum(co2_avr_list) / len(co2_avr_list)  # sum of ghg data
            round_avr_co2 = round((avr_co2), 2)
            print('Average CO2 emissions: {} per economic unit'.format(round_avr_co2))  # measurements?

        avr_co2_run()
        options_input()

    elif option == '5':
        def max_ghg_run():
            data = read_data()  # becomes tag for previous def

            max_ghg_list = max(data, key=lambda x: x['ghg'])

            print('Max GHG emissions: {} per economic unit of {} in {}'.format(max_ghg_list['ghg'], max_ghg_list['industry'], max_ghg_list['year']))

        max_ghg_run()
        options_input()

    elif option == '6':
        def max_co2_run():
            data = read_data()  # becomes tag for previous def

            max_co2_list = max(data, key=lambda x: x['co2'])

            print('Max CO2 emissions: {} per economic unit of {} in {}'.format(max_co2_list['co2'], max_co2_list['industry'], max_co2_list['year']))

        max_co2_run()
        options_input()

    elif option == '7':
        def min_ghg_run():
            data = read_data()  # becomes tag for previous def

            min_ghg_list = min(data, key=lambda x: x['ghg'])

            print('Min GHG emissions: {} per economic unit of {} in {}'.format(min_ghg_list['ghg'], min_ghg_list['industry'], min_ghg_list['year']))

        min_ghg_run()
        options_input()

    elif option == '8':
        def min_co2_run():
            data = read_data()  # becomes tag for previous def

            min_co2_list = min(data, key=lambda x: x['co2'])

            print('Min CO2 emissions: {} per economic unit of {} in {}'.format(min_co2_list['co2'], min_co2_list['industry'], min_co2_list['year']))

        min_co2_run()
        options_input()

    elif option == 'Bye':
        print('Thank you for taking part. Goodbye!')

    else:
        s_print('Please input 1 to 8. If you wish to exit, input Bye. ')
        options_input()

options_input()
#
# def total_run ():
#     data = read_data() #becomes tag for previous def
#
#     ghg = [] #creates blank list to add csv data - gfg
#     co2 = [] #creates blank list to add csv data - co2
#
#     for row in data:
#         greenhousegas = float(row['ghg']) #float not int because of decimal
#         ghg.append(greenhousegas) #append ghg emissions csv data into list
#
#         carbondioxide = float(row['co2'])
#         co2.append(carbondioxide) #append co2 emissions csv data into list
#
#     # 600 entries = len(ghg) and len(co2)
#     # print(ghg)
#     # print(co2)
#
#     total_ghg = sum(ghg) #sum of ghg data
#     round_total_ghg = round((total_ghg), 2)
#     print('Total greenhouse gas emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_total_ghg)) #measurements?
#
#     total_co2 = sum(co2) #sum of ghg data
#     round_total_co2 = round((total_co2), 2)
#     print('Total carbon dioxide emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_total_co2)) #measurements?
#
#     avr_ghg = sum(ghg) / len(ghg) #sum of ghg data
#     round_avr_ghg = round((avr_ghg), 2)
#     print('Average greenhouse gas emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_avr_ghg)) #measurements?
#
#     avr_co2 = sum(co2) / len(co2) #sum of ghg data
#     round_avr_co2 = round((avr_co2), 2)
#     print('Average carbon dioxide emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_avr_co2)) #measurements?
#
#     max_ghg = max(ghg)  # sum of ghg data
#     round_max_ghg = round((max_ghg), 2)
#     print('Max greenhouse gas emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_max_ghg))  # measurements?
#
#     max_co2 = max(co2)  # sum of ghg data
#     round_max_co2 = round((max_co2), 2)
#     print('Max carbon dioxide emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_max_co2))  # measurements?
#
# total_run()
#
#
# #
# # def max_run():
# #     max_ghg = max(total_run(ghg))   # max num in ghg data
# #     print(max_ghg)
# #
# #     if max_ghg in emissions_dict:
# #         industry_max = ['industry']
# #     return industry_max
# #
# #     max_ghg = max(total_run(ghg))  # sum of ghg data
# #     round_max_ghg = round((max_ghg), 2)
# #     print('Max greenhouse gas emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_max_ghg))  # measurements?
# #
# #     max_co2 = max(co2)  # sum of ghg data
# #     round_max_co2 = round((max_co2), 2)
# #     print('Max carbon dioxide emissions per unit of economic output across all industries, 1990 to 2018 and (provisional) 2019: {}'.format(round_max_co2))  # measurements?
# #
# # max_run()