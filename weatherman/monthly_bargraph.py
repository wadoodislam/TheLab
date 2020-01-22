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
months = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
          '5': 'May', '6': 'Jun', '7': 'Jul',
          '8': 'Aug', '9': 'Sep',
          '10': 'Oct', '11': 'Nov', '12': 'Dec'}
name_list = []
for name in os.listdir() :
    name_list.append(name)
    #print(name_list)
match = 'Murree_weather_' + year_no + '_' + months[month_no] + ".txt"

if match in name_list :
    print('Your results will be displayed soon !!!!')
else:
    print('Sorry !!! The file does not exists in our system')
    print('Thanks for using our service ...... Good Bye !!!!!')
    exit()

high_temp = 0
low_temp = 0
date1=''
date2=''

print('The Bar graph for  ' + year_no + '  ' + months[month_no] )
with open('Murree_weather_' + year_no + '_' + months[month_no] + ".txt" ) as scrap_data:
    c = 0
    got_list = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10',
                        'a11', 'a12', 'a13', 'a14','a15', 'a16','a17', 'a18', 'a19', 'a20',
                        'a21', 'a22', 'a23', 'a24', 'a25', 'a26', 'a27', 'a28', 'a29',
                        'a30', 'a31']
    for data in scrap_data :
        got_list[c] = data.split(',')
        z=got_list[c]
        if c>0 :
            print("\033[1;32;1m",z[0])
            if z[1] == '' :
                high_temp = 0
            else:
                high_temp = int(z[1])
            if z[3] == '' :
                low_temp = 0
            else:
                low_temp = int(z[3])
            for limit in range(high_temp) :
                print( "\033[1;31;1m",'+' , end=''  )
            print( "\033[1;31;1m","  " , high_temp)
            for limit in range(low_temp) :
                print( "\033[1;34;1m",'+' , end=''  )
            print( "\033[1;34;1m","  " , low_temp)




        c = c + 1




