import os
import sys
import csv

class Readings():

    def __init__(self, highest_temp, lowest_temp, max_humidity, min_humidity, date1, date2, date3, date4):
        self.highest_temp = highest_temp
        self.lowest_temp = lowest_temp
        self.max_humidity = max_humidity
        self.min_humidity = min_humidity
        self.date1 = date1
        self.date2 = date2
        self.date3 = date3
        self.date4 = date4

def output_result():
    print('Highest temprature was ',obj.highest_temp)
    print('recorded on the date   ',obj.date1)
    print('Lowest temprature was  ',obj.lowest_temp)
    print('recorded on the date   ',obj.date2)
    print('Maximum Humidity was   ',obj.max_humidity)
    print('recorded on the date   ',obj.date3)
    print('Minimum Humidity was   ',obj.min_humidity)
    print('recorded on the date   ',obj.date4)


def years(year_no):
    a = 11
    name_list = []
    for name in os.listdir(sys.argv[1]):
        if name.endswith(".txt"):
            file_name = name.split("_")

            if file_name[2] == year_no:
                x = file_name[0] + '_' + file_name[1] + '_' + file_name[2] + '_' + file_name[3]
                name_list.append(x)

    if year_no == '2004':
        a = 7
    if year_no == '2005':
        a = 9
    if year_no == '2016':
        a = 8
    for rep in range(0, a):

        with open(name_list[rep]) as scrap_data:

            for data in scrap_data:
                reader = csv.reader(scrap_data)
                for z in reader:

                    if z[1] != '' and obj.highest_temp < int(z[1]):
                        obj.highest_temp = int(z[1])
                        obj.date1 = z[0]

                    if z[3] != '' and obj.lowest_temp > int(z[3]):
                        obj.lowest_temp = int(z[3])
                        obj.date2 = z[0]

                    if z[7] != '' and obj.max_humidity < int(z[7]):
                        obj.max_humidity = int(z[7])
                        obj.date3 = z[0]

                    if z[9] != '' and obj.min_humidity > int(z[9]):
                        obj.min_humidity = int(z[9])
                        obj.date4 = z[0]

    return



def monthly(year_no , month_no)  :
    months = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
              '5': 'May', '6': 'Jun', '7': 'Jul',
              '8': 'Aug', '9': 'Sep',
              '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    name_list = []
    for name in os.listdir(sys.argv[1]) :
        name_list.append(name)
    match = 'Murree_weather_' + year_no + '_' + months[month_no] + ".txt"

    if match in name_list :
        print('Your results will be displayed soon !!!!')
    else:
        print('Sorry !!! The file does not exists in our system')
        print('Thanks for using our service ...... Good Bye !!!!!')
        exit()

    with open('Murree_weather_' + year_no + '_' + months[month_no] + ".txt" ) as scrap_data:
        for data in scrap_data:
            reader = csv.reader(scrap_data)
            for z in reader:

                if z[1] != '' and obj.highest_temp < int(z[1]):
                    obj.highest_temp = int(z[1])
                    obj.date1 = z[0]

                if z[3] != '' and obj.lowest_temp > int(z[3]):
                    obj.lowest_temp = int(z[3])
                    obj.date2 = z[0]

                if z[7] != '' and obj.max_humidity < int(z[7]):
                    obj.max_humidity = int(z[7])
                    obj.date3 = z[0]

                if z[9] != '' and obj.min_humidity > int(z[9]):
                    obj.min_humidity = int(z[9])
                    obj.date4 = z[0]

    return



def monthly_bar(year_no , month_no):

    months = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
              '5': 'May', '6': 'Jun', '7': 'Jul',
              '8': 'Aug', '9': 'Sep',
              '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    name_list = []
    for name in os.listdir(sys.argv[1]) :
        name_list.append(name)
    match = 'Murree_weather_' + year_no + '_' + months[month_no] + ".txt"

    if match in name_list :
        print('Your results will be displayed soon !!!!')
    else:
        print('Sorry !!! The file does not exists in our system')
        print('Thanks for using our service ...... Good Bye !!!!!')
        exit()



    print('The Bar graph for  ' + year_no + '  ' + months[month_no] )
    with open('Murree_weather_' + year_no + '_' + months[month_no] + ".txt" ) as scrap_data:
        for data in scrap_data:
            reader = csv.reader(scrap_data)
            for z in reader:
                if z[1] == '' :
                    obj.highest_temp = 0
                else:
                    obj.highest_temp = int(z[1])
                if z[3] == '' :
                    obj.lowest_temp = 0
                else:
                    obj.lowest_temp = int(z[3])
                print(z[0])
                for limit in range(obj.highest_temp) :
                    print('+' , end=''  )
                print("  " , obj.highest_temp)
                for limit in range(obj.lowest_temp) :
                    print('+' , end=''  )
                print("  " , obj.lowest_temp)


    return



def multiple_reports(year_no , month_no):

    name_list = []

    months = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
              '5': 'May', '6': 'Jun', '7': 'Jul',
              '8': 'Aug', '9': 'Sep',
              '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    for name in os.listdir(sys.argv[1]) :
        name_list.append(name)

    match = 'Murree_weather_' + year_no + '_' + months[month_no] + ".txt"

    if match in name_list :
        print(' ')
    else:
        print('Sorry !!! The file does not exists in our system')
        print('Thanks for using our service ...... Good Bye !!!!!')
        exit()

    with open('Murree_weather_' + year_no + '_' + months[month_no] + ".txt") as scrap_data:
        for data in scrap_data:
            reader = csv.reader(scrap_data)
            for z in reader:

                if z[1] != '' and obj.highest_temp < int(z[1]):
                    obj.highest_temp = int(z[1])
                    obj.date1 = z[0]

                if z[3] != '' and obj.lowest_temp > int(z[3]):
                    obj.lowest_temp = int(z[3])
                    obj.date2 = z[0]

                if z[7] != '' and obj.max_humidity < int(z[7]):
                    obj.max_humidity = int(z[7])
                    obj.date3 = z[0]

                if z[9] != '' and obj.min_humidity > int(z[9]):
                    obj.min_humidity = int(z[9])
                    obj.date4 = z[0]


    return




def main():

    if len(sys.argv) > 3 and sys.argv[2] != 'bar' :
        for arg in range(2,len(sys.argv)):
                given_date = sys.argv[arg]
                data1 = []
                data1 = given_date.split('/')
                year_no = data1[0]
                month_no = data1[1]
                multiple_reports(year_no, month_no)
        output_result()
        exit()
    elif sys.argv[2] == 'bar' :
            given_date = sys.argv[3]
            data1=[]
            data1 = given_date.split('/')
            year_no = data1[0]
            month_no = data1[1]
            monthly_bar(year_no , month_no)
            exit()
    elif '/' in sys.argv[2] :
            given_date = sys.argv[2]
            data1 = []
            data1 = given_date.split('/')
            year_no = data1[0]
            month_no = data1[1]
            monthly(year_no, month_no)
            output_result()
            exit()
    else:
            year_no = sys.argv[2]
            years(year_no)
            output_result()
            exit()

    return

obj = Readings(0, 50, 0, 100, 0, 0, 0, 0)
main()