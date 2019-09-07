import glob,sys
import datetime as date

class Report:
    def __init__(self):
          self.year_date=None
          self.year_coldest_day=None
          self.year_hotest_day=None
          self.year_highest_humidity_day=None
          self.year_highest_temperature=None
          self.year_lowest_temperature=None
          self.year_highest_humidity=None

          self.month_date=None
          self.month_avg_highest_temperature=None
          self.month_avg_lowest_temperature=None
          self.month_avg_humidity=None

          self.day_date=None
          self.day_highest_temperature=None
          self.day_lowest_temperature=None

    def check_year_hotest_day(self,highest_temperature):
        if  self.year_highest_temperature == None or\
           self.year_highest_temperature < highest_temperature :
            return True
        else:
            return False
    
    def check_year_coldest_day(self,coldest_temperature):
        if self.year_lowest_temperature == None or\
           self.year_lowest_temperature > coldest_temperature:
            return True
        else:
            return False

    def check_year_highest_humidity_day(self,highest_humidity):
        if self.year_highest_humidity == None or\
           self.year_highest_humidity < highest_humidity:
            return True
        else:
            return False

    def print_year_report(self):
          print("Year:{} \n Max temperature {} C at {} {} \n "\
                "Min temperature {} C at {} {} \n "\
                "Humidity {}% at {} {}".format(self.year_date.year,\
                 self.year_highest_temperature, self.year_hotest_day.strftime("%B"),\
                 self.year_hotest_day.day, self.year_lowest_temperature,\
                 self.year_coldest_day.strftime("%B"), self.year_hotest_day.day,\
                 self.year_highest_humidity, self.year_highest_humidity_day.strftime("%B"),\
                 self.year_highest_humidity_day.day))

    def print_month_report(self):
          print("Year:{} Month:{}  \n Avg Max temperature {} C \n"\
                " Avg Min temperature {} C \n Avg Mean Humidity {}%"\
                .format(self.month_date.year,self.month_date.strftime("%B"),\
                         self.month_avg_highest_temperature,\
                         self.month_avg_lowest_temperature,\
                         self.month_avg_humidity))

    def print_daily_report(self):
          print("\n Year :{} Month :{} Day :{} ".\
              format(self.day_date.year,self.day_date.strftime("%B"),\
                     self.day_date.day))

          print("Highest temperature:",end="")

          if self.day_highest_temperature==None:
              print("NO Record")

          elif self.day_highest_temperature<=0:
              for i in range(self.day_highest_temperature,0):
                  print ("+",end="")

          else:
              for i in range(self.day_highest_temperature):
                  print ("+",end="")

          print(" ",self.day_highest_temperature,"C")

          print("Coldest temperature:",end="")

          if self.day_lowest_temperature==None:
              print("NO Record")

          elif self.day_lowest_temperature<=0:
              for i in range(self.day_lowest_temperature,0):
                 print ("-",end="")

          else:
              for i in range(self.day_lowest_temperature):
                 print ("-",end="")
          print(" ",self.day_lowest_temperature,"C")



def year_data(file_path,action,input):
    year_report=Report()
    year_report.year_date=date.date(int(input),1,1)

    for file_name in glob.glob(file_path+"\Murree_weather_"+input+"_*"):
            file=open(file_name,"r")
            file_data=file.readline()

            for days in range(0,32):
                file_data=file.readline()
                file_data=file_data.split(',')
                if file_data[0]!="":
                    year_date=file_data[0]
                    highest_temp=file_data[1]
                    coldest_temp=file_data[3]
                    highest_humidity=file_data[7]

                    year_date=year_date.split("-") #spliting date in year month day
                    year=int(year_date[0])
                    month=int(year_date[1])
                    day=int(year_date[2])

                    if highest_temp !="":
                        if year_report.check_year_hotest_day(int(highest_temp)):
                            year_report.year_hotest_day=date.date(year,month,day)
                            year_report.year_highest_temperature=int(highest_temp)

                    if coldest_temp !="":
                        if year_report.check_year_coldest_day(int(coldest_temp)):
                            year_report.year_coldest_day=date.date(year,month,day)
                            year_report.year_lowest_temperature=int(coldest_temp)

                    if highest_humidity !="":
                        if year_report.check_year_highest_humidity_day(int(highest_humidity)):
                            year_report.year_highest_humidity_day=date.date(year,month,day)
                            year_report.year_highest_humidity=int(highest_humidity)

    year_report.print_year_report()


def month_data(file_path,action,year,month):
    avg_highest_temp=[]
    avg_lowest_temp=[]
    avg_mean_humidity=[]

    month_report=Report()
    month_report.month_date=date.date(int(year),int(month),1)
    for file_name in glob.glob(file_path + "\Murree_weather_" + year + "_"\
                               + month_report.month_date.strftime("%B")[:3]\
                               + "*"):
            file=open(file_name,"r")
            file_data=file.readline()

            for days in range(0,32):
                file_data=file.readline()
                file_data=file_data.split(',')
                if file_data[0]!="":
                    month_date=file_data[0]
                    highest_temp=file_data[1]
                    coldest_temp=file_data[3]
                    mean_humidity=file_data[8]


                    if highest_temp !="":
                        avg_highest_temp.append(int(highest_temp))
 
                    if coldest_temp !="":
                        avg_lowest_temp.append(int(coldest_temp))

                    if mean_humidity !="":
                        avg_mean_humidity.append(int(mean_humidity))
 
                    month_report=month_calculations(month_report,avg_highest_temp,
                                                    avg_lowest_temp,avg_mean_humidity)
    month_report.print_month_report()


def daily_data(file_path,action,year,month):

    daily_report=Report()
    daily_report.daily_date=date.date(int(year),int(month),1)
    for file_name in glob.glob(file_path + "\Murree_weather_" + year + "_"\
                               + daily_report.daily_date.strftime("%B")[:3]\
                               + "*"):
            file=open(file_name,"r")
            file_data=file.readline()

            for days in range(0,32):
                file_data=file.readline()
                file_data=file_data.split(',')
                if file_data[0]!="":
                    daily_date=file_data[0]
                    year_date=daily_date.split("-") #spliting date in year month day
                    year=int(year_date[0])
                    month=int(year_date[1])
                    day=int(year_date[2])

                    highest_temp=file_data[1]
                    coldest_temp=file_data[3]
                    mean_humidity=file_data[8]
                    daily_report.day_date=date.date(year,month,day)

                    if highest_temp !="":
                       daily_report.day_highest_temperature=int(highest_temp)                     
 
                    if coldest_temp !="":
                       daily_report.day_lowest_temperature=int(coldest_temp)

                    daily_report.print_daily_report()


def month_calculations(month,avg_highest_temp,
                       avg_lowest_temp,avg_mean_humidity):

    month.month_avg_highest_temperature=int(sum(avg_highest_temp)/ \
                                        len(avg_highest_temp))

    month.month_avg_lowest_temperature=int(sum(avg_lowest_temp)/ \
                                       len(avg_lowest_temp))

    month.month_avg_humidity=int(sum(avg_mean_humidity)/ \
                             len(avg_mean_humidity))
    return month


def year_input(input):
      year_name=int(input)
      try:
           if  year_name< 2004 or year_name> 2016:
              raise ValueError #this will send it 
         # to the print message and back to the input option
      except ValueError:
              print("Invalid integer. The number must be"\
                    "in the range of 2004-2016.")
              sys.exit()


def month_input(input):
       try:
              month_name=int(input)
              if  month_name <1  or  month_name > 12:
                   raise ValueError #this will send it to the print
              #                     message and back to the input option
       except ValueError:
              print("Invalid integer. The number must"\
                    " be in the range of 1 to 12.")
              sys.exit()


def weather_report(file_path,action,input):
       try:
           if  action!="--year" and action!="--month"\
                   and action!="--daily":
               raise ValueError
       except ValueError:
              print("Sytnax should be file_name file_path" \
                    "action could be ""--year,--month,--daily,"\
                    " Input \n e.g: weather.py " \
                    "D:\document --month 2011/2")
              sys.exit()

       if(action=="--year"):
            year_input(input)
            year_data(file_path,action,input)
        
       if(action=="--month"):
            input=input.split("/")
            year=input[0]
            month=input[1]
            year_input(year)
            month_input(month)
            month_data(file_path,action,year,month)

       if(action=="--daily"):
            input=input.split("/")
            year=input[0]
            month=input[1]
            year_input(year)
            month_input(month)
            daily_data(file_path,action,year,month)



def main():
    file_name=sys.argv[0]
    file_path=sys.argv[1]

    if len(sys.argv)<=4:
       action=sys.argv[2]
       input=sys.argv[3]
       weather_report(file_path,action,input)

    else:
       num_of_reports=len(sys.argv)-1
       for i in range(2,num_of_reports,2):
           action=sys.argv[i]
           input=sys.argv[i+1]
           weather_report(file_path,action,input)


main()