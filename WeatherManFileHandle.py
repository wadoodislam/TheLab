import glob
import csv
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
                data = WeatherManDataModel.DataModel(str(row["PKT"]), str(row["Max TemperatureC"]),
                                                     str(row["Mean TemperatureC"]), str(row["Min TemperatureC"]),
                                                     str(row["Dew PointC"]), str(row["MeanDew PointC"]),
                                                     str(row["Min DewpointC"]), str(row["Max Humidity"]),
                                                     str(row[" Mean Humidity"]), str(row[" Min Humidity"]),
                                                     str(row[" Max Sea Level PressurehPa"]),
                                                     str(row[" Mean Sea Level PressurehPa"]),
                                                     str(row[" Min Sea Level PressurehPa"]),
                                                     str(row[" Max VisibilityKm"]), str(row[" Mean VisibilityKm"]),
                                                     str(row[" Min VisibilitykM"]), str(row[" Max Wind SpeedKm/h"]),
                                                     str(row[" Mean Wind SpeedKm/h"]), str(row[" Max Gust SpeedKm/h"]),
                                                     str(row["Precipitationmm"]), str(row[" CloudCover"]),
                                                     str(row[" Events"]), str(row["WindDirDegrees"]))
                dataList.append(data)
        return dataList

