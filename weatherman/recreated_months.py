import os
import sys


class readings():
    highest_temp = 0
    lowest_temp = 30
    max_humidity = 0
    min_humidity = 100
    date1 = ''
    date2 = ''
    date3 = ''
    date4 = ''



def monthly(year_no , month_no)  :
    months = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
              '5': 'May', '6': 'Jun', '7': 'Jul',
              '8': 'Aug', '9': 'Sep',
              '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    name_list = []
    for name in os.listdir(sys.argv[1]) :
        name_list.append(name)
        #print(name_list)
    match = 'Murree_weather_' + year_no + '_' + months[month_no] + ".txt"

    if match in name_list :
        print('Your results will be displayed soon !!!!')
    else:
        print('Sorry !!! The file does not exists in our system')
        print('Thanks for using our service ...... Good Bye !!!!!')
        exit()



    with open('Murree_weather_' + year_no + '_' + months[month_no] + ".txt" ) as scrap_data:
        c = 0
        got_list = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10',
                            'a11', 'a12', 'a13', 'a14','a15', 'a16','a17', 'a18', 'a19', 'a20',
                            'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28', 'a29',
                            'a30', 'a31']
        for data in scrap_data :
            got_list[c] = data.split(',')
            z=got_list[c]
            if c > 0 and z[1] != '' and obj.highest_temp < int(z[1]):
                obj.highest_temp = int(z[1])
                obj.date1 = z[0]

            if c > 0 and z[3] != '' and obj.lowest_temp > int(z[3]):
                obj.lowest_temp = int(z[3])
                obj.date2 = z[0]

            if c > 0 and z[7] != '' and obj.max_humidity < int(z[7]):
                obj.max_humidity = int(z[7])
                obj.date3 = z[0]

            if c > 0 and z[9] != '' and obj.min_humidity > int(z[9]):
                obj.min_humidity = int(z[9])
                obj.date4 = z[0]

            c = c + 1


    print("Highest temprature was ",obj.highest_temp, " degree Centigrade recorded on ", obj.date1)
    print("Lowest temprature was ",obj.lowest_temp, " degree Centigrade recorded on ", obj.date2)
    print("Max Humidity level was ",obj.max_humidity, " recorded on ", obj.date3)
    print("Min Humidity level was ",obj.min_humidity, " recorded on ", obj.date4)

    mean_temp = (obj.highest_temp + obj.lowest_temp) / 2
    mean_humidity = (obj.max_humidity + obj.min_humidity) / 2
    print("Mean temprature was ",mean_temp, " degree Centigrade through out the month  ", months[month_no] , year_no)
    print("Mean Humidity level was ",mean_humidity, " through out the month ", months[month_no] , year_no)

    return

obj = readings

def main():
    while True:
        given_date = sys.argv[2]
        data1=[]
        data1 = given_date.split('/')
        year_no = data1[0]
        month_no = data1[1]
        monthly(year_no , month_no)
        exit()


    return

main()