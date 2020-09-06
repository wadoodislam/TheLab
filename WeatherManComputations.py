from datetime import datetime

import WeatherManFileHandle


class Computations:

    def __init__(self, path_to_dir):
        self.weatherman = WeatherManFileHandle.WeatherManFileHandle(path_to_dir)

    def get_data_for_year(self, year):
        year_data = []
        for file_name in self.weatherman.list_of_files:
            if str(year) in file_name:
                year_data.append(file_name)
        return self.weatherman.load_data(year_data)

    def get_data_for_month(self, year, month):
        dt = datetime.strptime(str(month), '%m')
        month_s = dt.strftime("%B")
        filename = "/Users/junaidikhlaq/PycharmProjects/TheLab/weatherfiles/Murree_weather_" + str(
            year) + "_" + month_s[:3] + ".txt"
        year_data = [filename]
        return self.weatherman.load_data(year_data)
