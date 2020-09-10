from WeatherRegister import WeatherRegister

OKBLUE = '\033[34m'
OKRED = '\033[31m'
Default = "\033[39m"


class WeatherReporter:
    def __init__(self, directory, year, month='*'):
        self.year_data = WeatherRegister(directory, year, month).data_list

    def problem_1(self):
        max_temp_data = max(filter(lambda x: x.max_temp, self.year_data), key=lambda x: int(x.max_temp))
        min_temp_data = min([data for data in self.year_data if data.min_temp], key=lambda x: int(x.min_temp))
        max_humid = max([data for data in self.year_data if data.max_humidity], key=lambda x: int(x.max_humidity))
        print("Highest: ", str(max_temp_data.max_temp) + " C on " + max_temp_data.pkt.strftime("%B %d"))
        print("Lowest: ", str(min_temp_data.min_temp) + " C on " + min_temp_data.pkt.strftime("%B %d"))
        print("Humid: ", str(max_humid.max_humidity) + " % on " + max_humid.pkt.strftime("%B %d"))

    def problem_2(self):
        max_avg_temp = max(filter(lambda x: x.mean_temp, self.year_data), key=lambda x: int(x.mean_temp))
        min_avg_temp = min(filter(lambda x: x.mean_temp, self.year_data), key=lambda x: int(x.mean_temp))
        print("Highest Average: " + str(max_avg_temp.mean_temp) + " C")
        print("Min Average: " + str(min_avg_temp.mean_temp) + " C")
        print("Average Mean Humidity: " + str(self.average_humidity()) + " %")

    def average_humidity(self):
        mean_humidities = [data.mean_humidity for data in filter(lambda x: x.mean_humidity, self.year_data)]
        return sum(mean_humidities, 0) / len(mean_humidities)

    def problem_3(self):

        print(self.year_data[0].pkt.strftime('%B %Y'))

        for data in self.year_data:
            if data.max_temp or data.min_temp:
                print(f"{data.pkt.day} {OKRED}{data.max_temp * '+'} {Default} {data.max_temp} C")
                print(f"{data.pkt.day} {OKBLUE}{data.min_temp * '+'} {Default} {data.min_temp} C")

    def bonus_task(self):
        print(self.year_data[0].pkt.strftime('%B %Y'))

        for data in self.year_data:
            if data.max_temp or data.min_temp:
                print(f"{data.pkt.strftime('%d')} {OKRED}")
                print(data.max_temp * "+")
                print(f"{OKBLUE}{data.min_temp * '+'} {Default} {data.max_temp} -{data.min_temp}C ")
