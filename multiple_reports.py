import os


def report():
    highest_temp = 0
    lowest_temp = 30
    max_humidity = 0
    min_humidity = 100
    date1=''
    date2=''
    date3=''
    date4=''
    name_list = []

    year_no = input('Enter year ... [ 2004-2016 ] : ')
    month_no = input("Enter month (1-12) = ")
    months = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
              '5': 'May', '6': 'Jun', '7': 'Jul',
              '8': 'Aug', '9': 'Sep',
              '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    for name in os.listdir() :
        name_list.append(name)

    match = 'Murree_weather_' + year_no + '_' + months[month_no] + ".txt"

    if match in name_list :
        print(' ')
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
            ret_data = [highest_temp , lowest_temp , max_humidity , min_humidity]
    return ret_data


months = input("How many comparisons you want  : ")
months = int(months)
result = []

for count in range(months) :
    result.append(report())
    #print(result)

print("         Highest_temprature    Lowest_temprature    Maximum_humidity     Minimum_humidity ")
for count in range(months) :
    d = result[count]
    for length in range(4) :
        print(    '            ' ,d[length] ,'       ', end='')

    print('\n')















