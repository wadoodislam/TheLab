import csv
import glob

from DataModel import WeatherData


class WeatherRegister:

    def __init__(self, directory, year, month='*'):
        self.data_list = []

        for file_path in glob.glob(f"{directory}/Murree_weather_{year}_{month}.txt"):
            for row in csv.DictReader(open(file_path, 'rt')):
                self.data_list.append(WeatherData(row))

        if not self.data_list:
            raise Exception(f"No Data Found for year: {year}.")
