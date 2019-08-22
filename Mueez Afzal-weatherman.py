import os
months={'1':'January', '2':'February','3':'March', '4':'April', '5':'May', '6':'June', '7':'July','8':'August', '9':'September','10':'October','11': 'November','12': 'December'}


class year:
    def __init__(self):
          self.name=None
          self.month_coldest=None
          self.month_hotest=None
          self.day_hot=None
          self.highest=None
          self.lowest=None
          self.day_cold=None
          self.day_humidity=None
          self.month_humidity=None
          self.humidity=None

    def get_name(self):
         return self.name
    
    def set_name(self, name):
          self.name=name

    def check_hot(self,highest):
        if  self.highest == None or self.highest < highest :
            return True
        else:
            return False
    
    def check_cold(self,coldest):
        if self.lowest == None or self.lowest > coldest:
            return True
        else:
            return False

    def check_humidity(self,humidity):
        if self.humidity == None or self.humidity < humidity:
            return True
        else:
            return False

     
    def set_highest(self,month_hotest,day_hot,highest):
       self.month_hotest=month_hotest  
       self.day_hot=day_hot
       self.highest=highest
    
    def set_lowest(self,month_coldest,day_cold,lowest):
       self.month_coldest=month_coldest  
       self.day_cold=day_cold
       self.lowest=lowest
   
    def set_humidity(self,month_humidity,day_humidity,humidity):
          self.day_humidity=day_humidity
          self.month_humidity=month_humidity
          self.humidity=humidity
    
    def print_name(self):
          print("Year:{} \n Max temperature {} C at {} {} \n Min temperature {} C at {} {} \n Humidity {}% at {} {}".format(self.name,self.highest,self.month_hotest,self.day_hot,self.lowest,self.month_coldest,self.day_cold,self.humidity,self.month_humidity,self.day_humidity))


    
        
  
class month:
    def __init__(self):
          self.year=None
          self.name=None
          self.avg_highest=None
          self.avg_lowest=None
          self.humidity=None

    def get_year(self):
         return self.year
    def get_month(self):
         return self.name
    
    def set_year(self, name):
          self.year=name

    def set_data(self,name,avg_lowest,avg_highest,humidity):
          self.name=name
          self.avg_highest=avg_highest
          self.avg_lowest=avg_lowest
          self.humidity=humidity
    def print_name(self):
          print("Year:{} Month:{}  \n Avg Max temperature {} C \n Avg Min temperature {} C \n Avg Mean Humidity {}% ".format(self.year,self.name,self.avg_highest,self.avg_lowest,self.humidity))

class day:
    def __init__(self):
          self.year=None
          self.month=None
          self.day=None
          self.highest=None
          self.lowest=None

    def get_year(self):
         return self.year

    def get_month(self):
         return self.month
 
    
    def set_year(self, name):
          self.year=name

    def set_hot(self,hot):
        self.highest=hot

    def set_cold(self,cold):
        self.lowest=cold

    def set_data(self,year,month,day):
          self.year=year
          self.month=month
          self.day=day

    def print_name(self):
          print("\n Year :{} Month :{} Day :{} ".format(self.year,self.month,self.day))
          print("Highest temperature:",end="")
          if self.highest==None:
              print("NO Record")
          elif self.highest<=0:
              for i in range(self.highest,0):
                  print ("+",end="")
          else:
              for i in range(self.highest):
                  print ("+",end="")
          print(" ",self.highest,"C")
          print("Coldest temperature:",end="")
          if self.lowest==None:
              print("NO Record")
          elif self.lowest<=0:
              for i in range(self.lowest,0):
                 print ("-",end="")
          else:
              for i in range(self.lowest):
                 print ("-",end="")
          print(" ",self.lowest,"C")

def file_data(day_list,month_list,year_list):
    day_count,month_count,year_count=0,0,0
    hot_list=[]
    cold_list=[]
    humidity_list=[]

    for filename in os.listdir("weatherfiles"):
        if filename.endswith(".txt"):
            year_name=filename.split("_")

            if year_count==0 or year_list[year_count-1].get_name() != year_name[2]:

                year_list.append(year_count)
                year_list[year_count]=year()
                year_list[year_count].set_name(year_name[2])
                year_count+=1 

            filename=("weatherfiles/"+filename)
            file=open(filename,"r")
            line=file.readline()

            month_list.append(month_count)
            month_list[month_count]=month()
            month_list[month_count].set_year(year_name[2])
                 
            for j in range(0,32):
                line=file.readline()
                line=line.split(',')

                if line[0] !="":

                    date=line[0].split("-")
                    month_name=months.get(date[1])

                    day_list.append(day_count)
                    day_list[day_count]=day()
                    day_list[day_count].set_data(year_name[2],month_name,date[2])
            
                    if line[1] !="":
                        day_list[day_count].set_hot(int(line[1]))
                        hot_list.append(int(line[1]))

                        if year_list[year_count-1].check_hot(int(line[1])):
                           year_list[year_count-1].set_highest(month_name,date[2],int(line[1]))

                    if line[3] !="":
                        day_list[day_count].set_cold(int(line[3]))
                        cold_list.append(int(line[3]))

                        if year_list[year_count-1].check_cold(int(line[3])):
                           year_list[year_count-1].set_lowest(month_name,date[2],int(line[3]))

                    if line[8] !="":
                        humidity_list.append(int(line[8]))

                    if line[7] !="":
                       if year_list[year_count-1].check_humidity(int(line[7])):
                          year_list[year_count-1].set_humidity(month_name,date[2],int(line[7]))

                    day_count+=1

            avg_hot=sum(hot_list)/len(hot_list)
            avg_cold=sum(cold_list)/len(cold_list)
            avg_humidity=sum(humidity_list)/len(humidity_list)
            month_list[month_count].set_data(month_name,int(avg_cold),int(avg_hot),int(avg_humidity))
            month_count+=1
    return year_list,month_list,day_list                

def weather_report(year_list):
    stop="y"
    input_list=[]
    while stop=="y" or stop=="Y":

         while True:
             try:
                year_name=int(input("Enter the Year from 2004 to 2016 :"))
                if year_name < 2004 or year_name > 2016:
                      raise ValueError #this will send it to the print message and back to the input option
                input_list.append(year_name)
                break
             except ValueError:
                     print("Invalid integer. The number must be in the range of 2004-2016.")
             
         stop=input("Want to enter more y/n :")

    for name in range(len(year_list)):
        for input_string in input_list:
           if str(input_string) == year_list[name].get_name():
               year_list[name].print_name()
               

             
def year_report(year_list):
  
    year_name=year_input()    
    for name in range(len(year_list)):
        if str(year_name) == year_list[name].get_name():
            year_list[name].print_name()
            break

def month_report(month_list):

    year_name=year_input()
    month_num=month_input()
 
    month_name=months.get(str(month_num))
    for name in range(len(month_list)):
        if str(year_name) == month_list[name].get_year() and str(month_name) == month_list[name].get_month():
            month_list[name].print_name()
            break
        if name==(len(month_list)-1):
            print("No record")
def day_report(day_list):
    year_name=year_input()
    month_name=month_input()
    month_name=months.get(str(month_name))
    for name in range(len(day_list)):
        if str(year_name) == day_list[name].get_year() and str(month_name) == day_list[name].get_month():
            day_list[name].print_name()           

def year_input():
    while True:
       try:
           year_name=int(input("Enter the Year 2004 to 2016:"))
           if  year_name< 2004 or year_name> 2016:
              raise ValueError #this will send it to the print message and back to the input option
           break
       except ValueError:
              print("Invalid integer. The number must be in the range of 2004-2016.")
    return year_name

def month_input():
   while True:
       try:
              month_name=int(input("Enter the month 1_12:"))
              if  month_name <1  or  month_name > 12:
                   raise ValueError #this will send it to the print message and back to the input option
              break
       except ValueError:
              print("Invalid integer. The number must be in the range of 1 to 12.")
   return month_name

def main():
    day_list=[]
    month_list=[]
    year_list=[]
    year_list,month_list,day_list=file_data(day_list,month_list,year_list)
    while True:
      try: 
         menu=int(input(" 1.A Year Report \n 2.A Month Report \n 3.A Month Daily Report \n 4.For Years Report \n "))
         if  menu< 1 or menu> 4:
              raise ValueError #this will send it to the print message and back to the input option
         break
      except ValueError:
              print("Invalid integer. The number must be in the range of 1->4.")
    if menu==1:
        year_report(year_list)
    elif menu==2:
       month_report(month_list)
    elif menu==3:
       day_report(day_list)
    elif menu==4:
        weather_report(year_list)
main()