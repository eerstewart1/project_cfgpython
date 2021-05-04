import sys
import time
import pandas as pd
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

    return data #data from csv put into nested dictionary

def cloud ():
    print('     ********     ********      **********       *********     ***********')
    print('  ***************************************************************************')
    print(' *****************!    ! !-- !   /--  /--\  !\    /! !-- **********************')
    print(' *****************! /\ ! !__ !   !   !    ! ! \  / ! !__       *****************')
    print(' *****************!/  \! !__ !__ \__  \__/  !  \/  ! !__ *********************')
    print(' *****************    ********* **********  *********  *******************')
    print(' *****   *****        *****     *****       *****      *****    *****')
    print(' ***     ***          ***       ***         ***        ***      ***')
    print(' !*!     !*!          !*!       !*!         !*!        !*!      !*!')
    print(' !*!     !*!          !*!       !*!         !*!        !*!      !*!')
    print(' !*!     !*!          !*!       !*!         !*!        !*!      !*!')
    print(' !*!     !*!          !*!       !*!         !*!        !*!      !*!')

cloud()

def interface ():
    s_print('Welcome! This is our Python project on CSV spreadsheet analysis.')
    s_print('Our topic is *Greenhouse Gas and CO2 Emissions Intensity by Industry* from the Office of National Statistics.')
    s_print('Greenhouse Gases are any gases that absorbs and emits heat into the atmosphere, keeping it warmer than normal.')
    s_print('Carbon dioxide is the most common greenhouse gas that humans emit by quantity and impact on global warming.')
    s_print('Our CSV contains greenhouse gas (GHG) and carbon dioxide (CO2) emissions output per unit of economic output.')
    s_print('Different industries, from retail to health care, were studied between 1990 to 2018, and 2019 provisionally.')
    s_print('What name shall I call you? ')
interface()

def input_username():
    username = input()
    user = username
    s_print('Hello {}! What would you like to know about Atmospheric emissions?'.format(user))
input_username()

def options ():
    print('1. Total GHG emissions per unit of economic output across all industries between 1990 and 2019.')
    print('2. Total CO2 emissions per unit of economic output across all industries between 1990 and 2019.')
    print('3. Average GHG emissions per unit of economic output across all industries between 1990 and 2019.')
    print('4. Average CO2 emissions per unit of economic output across all industries between 1990 and 2019.')
    print('5. Maximum GHG emissions per unit of economic output across all industries between 1990 and 2019.')
    print('6. Maximum CO2 emissions per unit of economic output across all industries between 1990 and 2019.')
    print('7. Minimum GHG emissions per unit of economic output across all industries between 1990 and 2019.')
    print('8. Minimum CO2 emissions per unit of economic output across all industries between 1990 and 2019.')
    print('9. Table and graph showing GHG and CO2 emissions by Year')
    print('10. Table and graph showing GHG and CO2 emissions by Industry')
    print('11. Table and graph showing GHG and CO2 emissions of Agriculture by year')
    print('12. Table and graph showing GHG and CO2 emissions in 2019 by Industry')
options()

def options_input():
    print('Please input 1 to 8. If you wish to exit, input Bye. ')
    option = input()

    if option == '1':
        def total_ghg_run():
            data = read_data()  # becomes tag for previous def
            ghg_total_list = []  # creates blank list to add csv data - ghg

            for row in data:
                greenhousegas = float(row['ghg'])  # float not int because of decimal
                ghg_total_list.append(greenhousegas)  #append ghg emissions csv data into list

            total_ghg = sum(ghg_total_list)  # sum of ghg data
            round_total_ghg = round((total_ghg), 2)
            s_print('Total GHG emissions: {} per 600 recorded economic units across all industries between 1990 to 2019.'.format(round_total_ghg))

        total_ghg_run()
        options_input()

    elif option == '2':
        def total_co2_run():
            data = read_data()
            co2_total_list = []

            for row in data:
                carbondioxide = float(row['co2'])
                co2_total_list.append(carbondioxide)

            total_co2 = sum(co2_total_list)
            round_total_co2 = round((total_co2), 2)
            s_print('Total CO2 emissions: {} per 600 recorded economic units across all industries between 1990 to 2019.'.format(round_total_co2))

            percent_co2 = int((100 / 536.02) * 321.22)

            s_print('That means {}% of GHG between 1990 and 2019 was C02.'.format(percent_co2))

        total_co2_run()
        options_input()

    elif option == '3':
        def avr_ghg_run():
            data = read_data()
            ghg_avr_list = []

            for row in data:
                greenhousegas = float(row['ghg'])
                ghg_avr_list.append(greenhousegas)

            avr_ghg = sum(ghg_avr_list) / len(ghg_avr_list)
            round_avr_ghg = round((avr_ghg), 2)
            s_print('Average greenhouse gas emissions: {} per economic unit'.format(round_avr_ghg))

            pddata = pd.read_csv('emissions.csv')

            df = pd.DataFrame(pddata)

            avr_df1 = df.drop((df[(df.ghg <= 0.79)]).index)
            avr_df2 = avr_df1.drop((avr_df1[(avr_df1.ghg >= 0.99)]).index)

            avr_df3 = pd.pivot_table(avr_df2, index=['year', 'industry'], values=['ghg'])
            print(avr_df3)

        avr_ghg_run()
        options_input()

    elif option == '4':
        def avr_co2_run():
            data = read_data()
            co2_avr_list = []

            for row in data:
                carbondioxide = float(row['co2'])
                co2_avr_list.append(carbondioxide)

            avr_co2 = sum(co2_avr_list) / len(co2_avr_list)
            round_avr_co2 = round((avr_co2), 2)
            s_print('Average CO2 emissions: {} per economic unit'.format(round_avr_co2))

            pddata = pd.read_csv('emissions.csv')

            df = pd.DataFrame(pddata)

            avr_df1 = df.drop((df[(df.co2 <= 0.44)]).index)
            avr_df2 = avr_df1.drop((avr_df1[(avr_df1.co2 >= 0.64)]).index)

            avr_df3 = pd.pivot_table(avr_df2, index=['year', 'industry'], values=['co2'])
            print(avr_df3)

        avr_co2_run()
        options_input()

    elif option == '5':
        def max_ghg_run():
            # data = read_data()
            #
            # max_ghg_list = max(data, key=lambda x: x['ghg'])
            #
            # s_print('Max GHG emissions: {} per economic unit of {} in {}'.format(max_ghg_list['ghg'], max_ghg_list['industry'], max_ghg_list['year']))

            data = pd.read_csv('emissions.csv')

            df = pd.DataFrame(data)

            maxghg_df = df.drop(df[df.ghg < 9].index)

            df1 = pd.pivot_table(maxghg_df, index=['year', 'industry'], values=['ghg'])
            print(df1)

        max_ghg_run()
        options_input()

    elif option == '6':
        def max_co2_run():
            # data = read_data()
            #
            # max_co2_list = max(data, key=lambda x: x['co2'])
            #
            # s_print('Max CO2 emissions: {} per economic unit of {} in {}'.format(max_co2_list['co2'], max_co2_list['industry'], max_co2_list['year']))

            data = pd.read_csv('emissions.csv')

            df = pd.DataFrame(data)

            maxco2_df = df.drop(df[df.co2 < 9].index)

            df1 = pd.pivot_table(maxco2_df, index=['year', 'industry'], values=['co2'])
            print(df1)

        max_co2_run()
        options_input()

    elif option == '7':
        def min_ghg_run():
            # data = read_data()
            #
            # min_ghg_list = min(data, key=lambda x: x['ghg'])
            #
            # s_print('Min GHG emissions: {} per economic unit of {} in {}'.format(min_ghg_list['ghg'], min_ghg_list['industry'], min_ghg_list['year']))

            data = pd.read_csv('emissions.csv')

            df = pd.DataFrame(data)

            minghg_df = df.drop(df[df.ghg != 0].index)

            df1 = pd.pivot_table(minghg_df, index=['year', 'industry'], values=['ghg'])
            print(df1)

        min_ghg_run()
        options_input()

    elif option == '8':
        def min_co2_run():
            # data = read_data()
            #
            # min_co2_list = min(data, key=lambda x: x['co2'])
            #
            # s_print('Min CO2 emissions: {} per economic unit of {} in {}'.format(min_co2_list['co2'], min_co2_list['industry'], min_co2_list['year']))
            data = pd.read_csv('emissions.csv')

            df = pd.DataFrame(data)

            minco2_df = df.drop(df[df.co2 != 0].index)

            df1 = pd.pivot_table(minco2_df, index=['year', 'industry'], values=['co2'])
            print(df1)

        min_co2_run()
        options_input()

    elif option == '9':
        def graph_year_run():
            # Initialize the lists for X and Y
            import matplotlib.pyplot as plt
            import numpy as np

            data = pd.read_csv('emissions.csv')

            df = pd.DataFrame(data)
            df1 = pd.pivot_table(df, index=['year'], values=['ghg', 'co2'], aggfunc=np.sum)
            print(df1)

            # Plot the data using bar() method
            df1.plot.bar(color=['b', 'g'])
            plt.title("GHG and CO2 Emissions by Year")
            plt.xlabel("Year")
            plt.ylabel("Emissions output")

            # Show the plot
            plt.show()

        graph_year_run()
        options_input()

    elif option == '10':
        def graph_industry_run():
            # Initialize the lists for X and Y
            import matplotlib.pyplot as plt
            import numpy as np

            data = pd.read_csv('emissions.csv')

            df = pd.DataFrame(data)

            df1 = pd.pivot_table(df, index=['industry'],values=['ghg', 'co2'],aggfunc=np.sum)
            print(df1)

            # Plot the data using bar() method
            df1.plot.bar(color=['b', 'g'])
            plt.title("GHG and CO2 Emissions by Industry")
            plt.xlabel("Industry")
            plt.ylabel("Emissions output")

            # Show the plot
            plt.show()

        graph_industry_run()
        options_input()

    elif option == '11':
        def graph_agriculture_run():
            # Initialize the lists for X and Y
            import matplotlib.pyplot as plt
            import numpy as np

            data = pd.read_csv('emissions.csv')

            df = pd.DataFrame(data)

            agriculture_df = df.drop(df[df.industry != 'agriculture'].index)
            print(agriculture_df)

            df1 = pd.pivot_table(agriculture_df, index=['year'],values=['ghg', 'co2'],aggfunc=np.sum)

            # Plot the data using bar() method
            df1.plot.bar(color=['b', 'g'])
            plt.title("GHG and CO2 Emissions in Agriculture")
            plt.xlabel("Year")
            plt.ylabel("Emissions output")

            # Show the plot
            plt.show()

        graph_agriculture_run()
        options_input()

    elif option == '12':
        def graph_recent_run():
            # Initialize the lists for X and Y
            import matplotlib.pyplot as plt
            import numpy as np

            data = pd.read_csv('emissions.csv')

            df = pd.DataFrame(data)

            recent_df = df.drop(df[df['year'] != 2019].index)
            print(recent_df)

            df1 = pd.pivot_table(recent_df, index=['industry'],values=['ghg', 'co2'],aggfunc=np.sum)

            # Plot the data using bar() method
            df1.plot.bar(color=['b', 'g'])
            plt.title("GHG and CO2 Emissions in 2019")
            plt.xlabel("Industry")
            plt.ylabel("Emissions output")

            # Show the plot
            plt.show()

        graph_recent_run()
        options_input()

    elif option == 'Bye':
        s_print('Thank you for taking part. Goodbye!')

    else:
        options_input()

options_input()
