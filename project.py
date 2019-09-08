import os
months={'1':'Jan', '2':'Feb','3':'Mar', '4':'Apr', '5':'May', '6':'Jun', '7':'Jul','8':'Aug', '9':'Sep','10':'Oct','11': 'Nov','12': 'Dec'}
def years_data():
    highest_temp=None
    lowest_temp=None
    humidity=None
    
    highest_temp_time=None
    lowest_temp_time=None
    humidity_time=None
    
    year=year_input()
    month_list=[]
    month_days_list=[]
    for filename in os.listdir("weatherfiles"):
       if filename.endswith(".txt"):
            year_name=filename.split("_")
            if str(year_name[2])==str(year):
               filename=("weatherfiles/"+filename)
               file=open(filename,"r")
               line=file.readline()
               for i in range(0,32):
                   line=file.readline()
                   line=line.split(',')
                   if line[0]!="":
                     
                     if line[1]!="":
                         if highest_temp is None or highest_temp<int(line[1]):
                             highest_temp_time=line[0]
                             highest_temp=int(line[1])
                     if line[3]!="":
                         if lowest_temp is None or lowest_temp>int(line[3]):
                             lowest_temp_time=line[0]
                             lowest_temp=int(line[3])
                     if line[7]!="":
                         if humidity is None or humidity<int(line[7]):
                             humidity_time=line[0]
                             humidity=int(line[7])
                   
    print("max temperature:{} C at {}".format(highest_temp,highest_temp_time))
    print("min temperature:{} C at {}".format(lowest_temp,lowest_temp_time))
    print("max humidity:{} % at {}".format(humidity,humidity_time))
                   
                   
def months_data():
    year=year_input()
    month=month_input()
    avg_max_temperature=0.0
    avg_min_temperature=0.0
    avg_humidity=0.0
    month_days=0
    for filename in os.listdir("weatherfiles"):
       if filename.endswith(".txt"):
            year_name=filename.split("_")
            if str(year_name[2])==str(year) and str(year_name[3])==str((months[str(month)]))+".txt":
               
               filename=("weatherfiles/"+filename)
               file=open(filename,"r")
               line=file.readline()
               for i in range(0,32):
                   line=file.readline()
                   line=line.split(',')
                   if line[0]!="":
                     
                     if line[1]!="":
                        month_days=month_days+1
                        avg_max_temperature=avg_max_temperature+float(line[1])
                     if line[3]!="":
                        avg_min_temperature=avg_min_temperature+float(line[3])
                     if line[8]!="":
                        avg_humidity=avg_humidity+float(line[8])
            
    print("Average max temperature:", avg_max_temperature/month_days , "C")
    print("Average min temperature:", avg_min_temperature/month_days ,"C") 
    print("Average mean humidity:", avg_humidity/month_days,"%")      
              

def days_data():
    year=year_input()
    month=month_input()
    for filename in os.listdir("weatherfiles"):
       if filename.endswith(".txt"):
            year_name=filename.split("_")
            if str(year_name[2])==str(year) and str(year_name[3])==str((months[str(month)]))+".txt":
               
               filename=("weatherfiles/"+filename)
               file=open(filename,"r")
               line=file.readline()
               for i in range(0,32):
                   line=file.readline()
                   line=line.split(',')
                   if line[0]!="":
                     if line[1]!="":
                       print(line[0]," ",end="")  
                       for j in range (0 , int(line[1])):
                          print("+",end="")
                       print(line[1],"C")
                       print(line[0]," ",end="")  
                       for j in range (0,int(line[3])):
                          print("+",end="")
                       print(line[3],"C")
def year_input():
    year=None
    while True:
       try:
           year=int(input("Enter the Year 2004 to 2016:"))
           if  year< 2004 or year> 2016:
              raise ValueError #this will send it to the print message and back to the input option
           break
       except ValueError:
              print("Invalid integer. The number must be in the range of 2004-2016.")
    return year

def month_input():
   month=None
   while True:
       try:
              month=int(input("Enter the month 1_12:"))
              if  month <1  or  month > 12:
                   raise ValueError #this will send it to the print message and back to the input option
              break
       except ValueError:
              print("Invalid integer. The number must be in the range of 1 to 12.")
   return month
       


def main():
    while True:
      try: 
         menu=int(input(" 1.A Year Report \n 2.A Month Report \n 3.A Month Daily Report \n 4.For Years Report \n "))
         if  menu< 1 or menu> 4:
              raise ValueError #this will send it to the print message and back to the input option
         break
      except ValueError:
              print("Invalid integer. The number must be in the range of 1->4.")
     
        
    if menu==2:
      months_data()
    elif menu==3:
      days_data()
    elif menu==1:
        years_data()
    
    
  
main()  