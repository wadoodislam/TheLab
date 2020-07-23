import  numpy as np
import pandas as pd
import os
from operator import attrgetter
from colorama import  Fore,Back,Style
import sys
import argparse
import calendar
from datetime import datetime


#parsing Arguments
parser=argparse.ArgumentParser()
parser.add_argument("-a","--avg")
parser.add_argument("-e","--year")
parser.add_argument("-c","--charts")

args=vars(parser.parse_args())

print(args["avg"])
print(args["year"])
print(args["charts"])



path = 'd:\\Softcreed\\Weather-Task1\\weatherfiles\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))


class WeatherData:
    def __init__(self, pkt=None, maxTemp=None, meanTemp=None,
                 minTemp=None, dewPoint=None, meanDewPoint=None,
                 minDewPoint=None, maxHumid=None, meanHumid=None,
                 minHumid=None,
                 maxSeaLevelP=None, meanSeaLevelP=None,
                 minSeaLevelP=None, maxVisibilityKm=None,
                 meanVisibilityKm=None, minVisibilityKm= None, maxWindSpeedKmph=None,
                 meanWindSpeedKmph=None, maxGustSpeedKmph=None,
                 precipitation=None, cloudCover=None,
                 events=None, windDirectionDegree=None):
        self.pkt=(pkt)
        self.maxTemp=(maxTemp)
        self.meanTemp=(meanTemp)
        self.minTemp=(minTemp)
        self.dewPoint=(dewPoint)
        self.meanDewPoint=(meanDewPoint)
        self.minDewPoint=(minDewPoint)
        self.maxHumid=(maxHumid)
        self.meanHumid= (meanHumid)
        self.minHumid=(minHumid)
        self.maxSeaLevelP=(maxSeaLevelP)
        self.meanSeaLevelP=(meanSeaLevelP)
        self.minSeaLevelP=(minSeaLevelP)
        self.maxVisibilityKm=(maxVisibilityKm)
        self.meanVisibilityKm=(meanVisibilityKm)
        self.minVisibilityKm=(minVisibilityKm)
        self.maxWindSpeedKmph=(maxWindSpeedKmph)
        self.meanWindSpeedKmph=(meanWindSpeedKmph)
        #self.minWindSpeedKmph
        self.maxGustSpeedKmph=(maxGustSpeedKmph)
        self.precipitationMM=(precipitation)
        self.cloudCover=(cloudCover)
        self.events=(events)
        self.windDirectionDegrees=(windDirectionDegree)

    def __str__(self):
        return str(self.pkt)+" "+str(self.precipitationMM)+" "+str(self.minTemp)


weatherDataList = []

header=open(files[0]).readline()

#weatherDataList.append((header.split(',')))

#test=pd.read_csv("WorldCups.csv")
#print(test["Year"])



for f in files:
    openFile = pd.read_csv(f)
    for i,row in openFile.iterrows():
        weatherDataList.append(WeatherData(row[0],row["Max TemperatureC"],row["Mean TemperatureC"],row["Min TemperatureC"], row["Dew PointC"],
                                     row["MeanDew PointC"],row["Min DewpointC"],row["Max Humidity"],row[" Mean Humidity"], row[" Min Humidity"],
                                     row[" Max Sea Level PressurehPa"], row[" Mean Sea Level PressurehPa"], row[" Min Sea Level PressurehPa"],
                                     row[" Max VisibilityKm"],row[" Mean VisibilityKm"],row[" Min VisibilitykM"],
                                     row[" Max Wind SpeedKm/h"], row[" Mean Wind SpeedKm/h"], row[" Max Gust SpeedKm/h"],
                                     row["Precipitationmm"], row[" CloudCover"], row[" Events"], row["WindDirDegrees"]))





    # for weatherData in weatherDataList:
    #     print(weatherData)
    # # #weatherDataList.append(WeatherData(lines))

#df = pd.DataFrame(weatherDataList)






#highest and Lowest Temperatures


reportingList=[]

if args["year"] is not None:

    for weatherData in weatherDataList:
        if args["year"] in weatherData.pkt:
            #print(weatherData)
            reportingList.append(weatherData)


    highestTemp=max(reportingList,key=attrgetter('maxTemp'))
    lowestTemp=min(reportingList,key=attrgetter('minTemp'))
    maxhumid=max(reportingList,key=attrgetter('maxHumid'))

    print("Report :1")
    print("Highest Temperature: ", highestTemp.maxTemp," on ", highestTemp.pkt )
    print("Lowest Temperature: ", lowestTemp.minTemp," on ", lowestTemp.pkt)
    print("Humidity: ",maxhumid.maxHumid," on ", maxhumid.pkt)

#Average highest,lowest temperature and average mean humidity

reportingList.clear()

if args["avg"] is not None:
    highestList=[]
    lowestList=[]
    humidList=[]

    str=str(args["avg"])
    data=str.split("/")
    year=data[0]
    month=data[1]
    key=year+"-"+month
    for weatherData in weatherDataList:
        if key in weatherData.pkt:
            #print(weatherData.pkt)
            reportingList.append(weatherData)
            highestList.append(weatherData.maxTemp)
            lowestList.append(weatherData.minTemp)
            humidList.append(weatherData.meanHumid)





    averageHighestTemperature= sum(highestList)/len(highestList)
    averageLowestTemperature= sum(lowestList)/len(lowestList)
    averageMeanHumidity= sum(humidList)/len(humidList)

    print("Report 2: Average")
    print("Average Temperature in given month: ",round(averageHighestTemperature,2))
    print("Average Lowest Temperature in given month: ",round(averageLowestTemperature,2))
    print("Average Mean Humidity in given month: ",round(averageMeanHumidity,2))

#Report 3
#using reporting list variable we made in previous reporting loop

if args["charts"] is not None:

    str = args["charts"]
    data = str.split("/")
    year = data[0]
    month = data[1]
    key = year + "-" + month
    count=0
    reportingList.clear()

    for weatherData in weatherDataList:
        if key in weatherData.pkt:
            #print(weatherData)
            reportingList.append(weatherData)

    for weatherPerDay in reportingList:
        if count<10:
            print(Fore.RESET,weatherPerDay.pkt[-1:],end=' ')
        else:
            print(Fore.RESET, weatherPerDay.pkt[-2:], end=' ')
        for i in range(0,weatherPerDay.maxTemp):
            print( Fore.RED,"+",end="",sep='')
        print(weatherPerDay.maxTemp)

        if count < 10:
            print(Fore.RESET, weatherPerDay.pkt[-1:], end=' ')
        else:
            print(Fore.RESET, weatherPerDay.pkt[-2:], end=' ')
        for i in range(0,weatherPerDay.minTemp):
            print( Fore.BLUE,"+",end="",sep='')
        print(weatherPerDay.minTemp)
        count+=1

    #Report 5 Bonus Task

    count=0
    print(calendar.month_name[int(month)]," ",year)
    for weatherPerDay in reportingList:
        if count<10:
            print(Fore.RESET,weatherPerDay.pkt[-1:],end=' ')
        else:
            print(Fore.RESET, weatherPerDay.pkt[-2:], end=' ')
        for i in range(0,weatherPerDay.maxTemp):
            print( Fore.RED,"+",end="",sep='')

        for i in range(0,weatherPerDay.minTemp):
            print( Fore.BLUE,"+",end="",sep='')
        print(" ",weatherPerDay.maxTemp, "C - ", weatherPerDay.minTemp, "C ", end='')

        print("")
        count+=1





