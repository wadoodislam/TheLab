import csv
import glob

import WeatherManDataModel


class WeatherManFileHandle:

    # Get Directory as an constructor parameter and get all the files in that directory
    def __init__(self, directory):
        self.list_of_files = glob.glob(directory)
        self.list_of_files.sort()

    # Read and load data into Array
    def load_data(self, files_list):
        dataList = []
        for file_path in files_list:
            file = csv.DictReader(open(file_path, 'rt'))
            for row in file:
                data = WeatherManDataModel.WeatherData(row)
                dataList.append(data)
        return dataList

