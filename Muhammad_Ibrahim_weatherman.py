import os


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

def file_data(daily_list,monthly_list,yearly_list):
    d_count,m_count,y_count=0,0,0
    highest_list=[]
    coldest_list=[]
    humidity_list=[]

    for folder_name in os.listdir("weatherfiles"):
        if folder_name.endswith(".txt"):
            year_name=folder_name.split("_")

            if y_count==0 or yearly_list[y_count-1].get_name() != year_name[2]:

                yearly_list.append(y_count)
                yearly_list[y_count]=year()
                yearly_list[y_count].set_name(year_name[2])
                y_count+=1 

            folder_name=("weatherfiles/"+folder_name)
            file=open(folder_name,"r")
            per_line=file.readline()

            monthly_list.append(m_count)
            monthly_list[m_count]=month()
            monthly_list[m_count].set_year(year_name[2])
                 
            for j in range(0,32):
                per_line=file.readline()
                per_line=per_line.split(',')

                if per_line[0] !="":

                    date=per_line[0].split("-")
                    month_name=select_month.get(date[1])

                    daily_list.append(d_count)
                    daily_list[d_count]=day()
                    daily_list[d_count].set_data(year_name[2],month_name,date[2])
            
                    if per_line[1] !="":
                        daily_list[d_count].set_hot(int(per_line[1]))
                        highest_list.append(int(per_line[1]))

                        if yearly_list[y_count-1].check_hot(int(per_line[1])):
                           yearly_list[y_count-1].set_highest(month_name,date[2],int(per_line[1]))

                    if per_line[3] !="":
                        daily_list[d_count].set_cold(int(per_line[3]))
                        coldest_list.append(int(per_line[3]))

                        if yearly_list[y_count-1].check_cold(int(per_line[3])):
                           yearly_list[y_count-1].set_lowest(month_name,date[2],int(per_line[3]))

                    if per_line[8] !="":
                        humidity_list.append(int(per_line[8]))

                    if per_line[7] !="":
                       if yearly_list[y_count-1].check_humidity(int(per_line[7])):
                          yearly_list[y_count-1].set_humidity(month_name,date[2],int(per_line[7]))

                    d_count+=1

            avg_hot=sum(highest_list)/len(highest_list)
            avg_cold=sum(coldest_list)/len(coldest_list)
            avg_humidity=sum(humidity_list)/len(humidity_list)
            monthly_list[m_count].set_data(month_name,int(avg_cold),int(avg_hot),int(avg_humidity))
            m_count+=1
    return yearly_list,monthly_list,daily_list                

def Total_report(yearly_list):
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

    for name in range(len(yearly_list)):
        for input_string in input_list:
           if str(input_string) == yearly_list[name].get_name():
               yearly_list[name].print_name()
               

             
def yearly_report(yearly_list):
  
    year_name=yearly_input()    
    for name in range(len(yearly_list)):
        if str(year_name) == yearly_list[name].get_name():
            yearly_list[name].print_name()
            break

def monthly_report(monthly_list):

    year_name=yearly_input()
    month_num=monthly_input()
 
    month_name=select_month.get(str(month_num))
    for name in range(len(monthly_list)):
        if str(year_name) == monthly_list[name].get_year() and str(month_name) == monthly_list[name].get_month():
            monthly_list[name].print_name()
            break
        if name==(len(monthly_list)-1):
            print("No record")
def daily_report(daily_list):
    year_name=yearly_input()
    month_name=monthly_input()
    month_name=select_month.get(str(month_name))
    for name in range(len(daily_list)):
        if str(year_name) == daily_list[name].get_year() and str(month_name) == daily_list[name].get_month():
            daily_list[name].print_name()           

def yearly_input():
    while True:
       try:
           year_name=int(input("Enter the Year 2004 to 2016:"))
           if  year_name< 2004 or year_name> 2016:
              raise ValueError #this will send it to the print message and back to the input option
           break
       except ValueError:
              print("Invalid integer. The number must be in the range of 2004-2016.")
    return year_name

def monthly_input():
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
    daily_list=[]
    monthly_list=[]
    yearly_list=[]
    yearly_list,monthly_list,daily_list=file_data(daily_list,monthly_list,yearly_list)
    while True:
      try: 
         menu=int(input(" 1.A Year Report \n 2.A Month Report \n 3.A Month Daily Report \n 4.For Years Report \n "))
         if  menu< 1 or menu> 4:
              raise ValueError #this will send it to the print message and back to the input option
         break
      except ValueError:
              print("Invalid integer. The number must be in the range of 1->4.")
    if menu==1:
        yearly_report(yearly_list)
    elif menu==2:
       monthly_report(monthly_list)
    elif menu==3:
       daily_report(daily_list)
    elif menu==4:
        Total_report(yearly_list)

select_month={'1':'January', '2':'February','3':'March', '4':'April', '5':'May', '6':'June', '7':'July','8':'August', '9':'September','10':'October','11': 'November','12': 'December'}
main()