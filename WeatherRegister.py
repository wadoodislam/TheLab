import csv
import glob

from DataModel import WeatherData


class WeatherRegister:

    def __init__(self, directory):
        self.list_of_files = glob.glob(directory)
        # for r in self.list_of_files:
        #     print(r)
        self.data_list = []
        for file_path in self.list_of_files:
            file = csv.DictReader(open(file_path, 'rt'))
            for row in file:
                data = WeatherData(row)
                self.data_list.append(data)
