import csv
import os
import pandas
import glob
from statistics import mean

class WeatherReading:
	def __init__(self,row):
		self.date=row['PKT']
		self.max_temp=row['Max TemperatureC']
		self.min_temp=row['Min TemperatureC']
		self.mean_hum=row[' Mean Humidity']
		self.max_hum=row['Max Humidity']

	def __str__(self):
		return f'{self.date}, {self.max_temp}, {self.min_temp}, {self.mean_hum}, {self.max_hum}'

	def write_dict(self):
		weather_dict={'date' : self.date, 'max_temp' : self.max_temp, 'min_temp' : self.min_temp, 'mean_hum' : self.mean_hum, 'max_hum' : self.max_hum}
		return weather_dict
	

class Reader:
		
	def __init__(self,opt,path,year,month="*"):
		_weather_data = []	
		for file_name in glob.glob(os.path.join(path, f'Murree_weather_{year}_{month}.txt')):
			with open(file_name,'r') as new_file:
				for row in csv.DictReader(new_file):
					obj=WeatherReading(row)
					self._weather_data.append(obj.write_dict())

		return _weather_data
		
		

class Calculator:
	def calculate_for_e(self,_weather_files):
		highest_temp={'max_temp': '-100'}
		lowest_temp={'min_temp':'100'}
		highest_hum={'max_hum':'0'}
		for row in _weather_files:
			if row['max_temp'] > highest_temp['max_temp']: #Finding Highest Temperature
				highest_temp=row
			if row['min_temp'] < lowest_temp['min_temp']: #Finding Lowest Temperature
				lowest_temp=row
			if row['max_hum'] > highest_hum['max_hum']: #Findind maximum huidity
				highest_hum=row
		
		return highest_temp,lowest_temp,highest_hum

	def calculate_for_a(self,_weather_files):
		avg_high=[]
		avg_low=[]
		avg_mean_hum=[]
		for row in _weather_files:
			avg_high.append(int(row['max_temp']))
			avg_low.append(int(row['min_temp']))
			avg_mean_hum.append(int(row['mean_hum']))

		return avg_high,avg_low,avg_mean_hum

		Reporter().reporter_for_a(int(mean(avg_high)),int(mean(avg_low)),int(mean(avg_mean_hum)))


class Reporter:	
	def __init__(self,weather_data):
		self.calculator=Calculator(weather_data)
	def reporter_for_e(self,highest_temp,lowest_temp,highest_hum):
		highest_temp, lowest_temp, highest_hum=self.calculator.calculate_for_e()
		print(f"Highest: {highest_temp['max_temp']}C on  {highest_temp['date']}")
		print(f"Lowest: {lowest_temp['min_temp']}C on  {lowest_temp['date']}")
		print(f"Humidity: {highest_hum['max_hum']}% on {highest_hum['date']}")

	def reporter_for_a(self,avg_high,avg_low,avg_mean_hum):
		avg_high,avg_low,avg_mean_hum=self.calculator.calculate_for_a()
		print(f"Highest Average: {avg_high}C")
		print(f"Lowest Average: {avg_low}C")
		print(f"Average Mean Humidity: {avg_mean_hum}%")

		


def main():
	weather_data=Reader('-a','D:\\Data\\Study Data\\TheLab\\weatherfiles','2016','Mar')

	if opt=='-e':
			Calculator().calculate_for_e(self._weather_data)
		elif opt=='-a':
			Calculator().calculate_for_a(self._weather_data)


if __name__ == '__main__':
	main()