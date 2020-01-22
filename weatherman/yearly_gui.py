import os
from tkinter import *
import tkinter as tk


root=Tk()
root.geometry("500x550")
root.title("Years Report")

head = Label(root , text = 'You may enter any year from 2004-2016 ')
head.pack()
year = Entry(root)
year.pack()


def value () :
    global year
    year_no = year.get()
    print (year_no)
    year = year_no


b = Button(root,text='Verify',command=value)
b.pack()

result = Label(root , text = 'The results will be displayed here')
result.pack()


def report():

    global year
    name_list=[]


    #def loading_files(year_no):
    for name in os.listdir('weatherfiles'):
        if name.endswith(".txt"):
            #print(name)
            file_name = name.split("_")

            if file_name[2] == year :
                x= file_name[0] + '_' + file_name[1] + '_' +  file_name[2] + '_' + file_name[3]
                name_list.append(x)
                #print(name_list)


    highest_temp = 0
    lowest_temp = 30
    max_humidity = 0
    min_humidity = 100
    date1=''
    date2=''
    date3=''
    date4=''
    a=11
    if year == '2004'  :
        a=7
    if year == '2005'  :
        a=9
    if year == '2016'  :
        a=8
    for rep in range(0,a) :

        with open(name_list[rep]) as scrap_data:

            c=0
            got_list=['a0', 'a1', 'a2', 'a3', 'a4', 'a5','a6', 'a7', 'a8', 'a9', 'a10', 'a11','a12', 'a13', 'a14', 'a15','a16', 'a17', 'a18', 'a19', 'a20', 'a21', 'a22', 'a23', 'a24', 'a25','a26', 'a27', 'a28', 'a29', 'a30', 'a31']

            for data in scrap_data:                                 #iterate through data
                got_list[c] = data.split(',')
                #print (got_list[c])
                z=got_list[c]
                if c>0 and z[1]!= '' and highest_temp < int(z[1]) :
                    highest_temp= int(z[1])
                    date1 = z[0]

                if c>0 and z[3]!= '' and lowest_temp > int(z[3]) :
                    lowest_temp = int(z[3])
                    date2 = z[0]

                if c>0 and z[7]!= '' and max_humidity < int(z[7]) :
                    max_humidity = int(z[7])
                    date3 = z[0]

                if c>0 and z[9]!= '' and min_humidity > int(z[9]) :
                    min_humidity = int(z[9])
                    date4 = z[0]

                c = c + 1

    T = tk.Text(root, height=25, width=60)
    T.pack()
    T.insert(tk.END, "Highest temprature was \n" )
    T.insert(tk.END, highest_temp )
    T.insert(tk.END, " \n" )
    T.insert(tk.END, "recorded on \n" )
    T.insert(tk.END, date1)
    T.insert(tk.END, " \n" )
    T.insert(tk.END, " \n" )
    T.insert(tk.END, "Lowest temprature was \n")
    T.insert(tk.END, lowest_temp)
    T.insert(tk.END, " \n" )
    T.insert(tk.END, "recorded on \n")
    T.insert(tk.END, date2)
    T.insert(tk.END, " \n" )
    T.insert(tk.END, " \n" )
    T.insert(tk.END, "Max Humidity level was \n")
    T.insert(tk.END, max_humidity)
    T.insert(tk.END, " \n" )
    T.insert(tk.END, "recorded on \n")
    T.insert(tk.END, date3)
    T.insert(tk.END, " \n" )
    T.insert(tk.END, " \n" )
    T.insert(tk.END, "Min Humidity level was \n ")
    T.insert(tk.END, min_humidity)
    T.insert(tk.END, " \n" )
    T.insert(tk.END, "recorded on \n")
    T.insert(tk.END, date4)
    T.insert(tk.END, " \n" )
    T.insert(tk.END, " \n" )
    mean_temp = (highest_temp + lowest_temp) / 2
    mean_humidity = (max_humidity + min_humidity) / 2
    T.insert(tk.END, "Mean temprature was \n")
    T.insert(tk.END, mean_temp)
    T.insert(tk.END, " \n" )
    T.insert(tk.END, " \n" )
    T.insert(tk.END, "Mean Humidity level was \n ")
    T.insert(tk.END, mean_humidity)
    T.insert(tk.END, " \n" )




c = Button(root,text='Generate',command=report)
c.pack()



mainloop()






