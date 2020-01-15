import os



year_no = input('You can generate the monthly weather report of muree [ years 2004-2016 ] : ')
if int(year_no) < 2004 or int(year_no) > 2016 or year_no == '' :
    print("Try to be smart but not oversmart ")
    print("I'm a trained bot give me a valid input ")
    year_no = input('years ... [ 2004-2016 ] : ')
if int(year_no) < 2004 or int(year_no) > 2016 or year_no == '' :
    print("Again you provided a wrong value")
    print("I got other things to do as well i prefer to do them other then playing this")
    print("It was fun working with you ...... Good Bye !!!!!")
    exit()
month_no = input("Enter month (1-12) = ")

highest_temp = 0
lowest_temp = 30
max_humidity = 0
min_humidity = 100
date1=''
date2=''
date3=''
date4=''
months = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
          '5': 'May', '6': 'Jun', '7': 'Jul',
          '8': 'Aug', '9': 'Sep',
          '10': 'Oct', '11': 'Nov', '12': 'Dec'}

with open('Murree_weather_' + year_no + '_' + months[month_no] + ".txt" ) as scrap_data:
    c = 0
    got_list = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10',
                        'a11', 'a12', 'a13', 'a14','a15', 'a16','a17', 'a18', 'a19', 'a20',
                        'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28', 'a29',
                        'a30', 'a31']
    for data in scrap_data :
        got_list[c] = data.split(',')
        z=got_list[c]
        if c > 0 and z[1] != '' and highest_temp < int(z[1]):
            highest_temp = int(z[1])
            date1 = z[0]

        if c > 0 and z[3] != '' and lowest_temp > int(z[3]):
            lowest_temp = int(z[3])
            date2 = z[0]

        if c > 0 and z[7] != '' and max_humidity < int(z[7]):
            max_humidity = int(z[7])
            date3 = z[0]

        if c > 0 and z[9] != '' and min_humidity > int(z[9]):
            min_humidity = int(z[9])
            date4 = z[0]

        c = c + 1


print("Highest temprature was ",highest_temp, " degree Centigrade recorded on ", date1)
print("Lowest temprature was ",lowest_temp, " degree Centigrade recorded on ", date2)
print("Max Humidity level was ",max_humidity, " recorded on ", date3)
print("Min Humidity level was ",min_humidity, " recorded on ", date4)

mean_temp = (highest_temp + lowest_temp) / 2
mean_humidity = (max_humidity + min_humidity) / 2
print("Mean temprature was ",mean_temp, " degree Centigrade through out the month  ", months[month_no] , year_no)
print("Mean Humidity level was ",mean_humidity, " through out the month ", months[month_no] , year_no)
