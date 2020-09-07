from datetime import datetime

OKBLUE = '\033[34m'
OKRED = '\033[31m'
Default = "\033[39m"


class WeatherReporter:

    def problem_1(self, year_data):
        max_temp_data = max(year_data, key=lambda x: int(x.max_temp) if x.max_temp else -200)
        min_temp_data = min(year_data, key=lambda x: int(x.min_temp) if x.min_temp else 200)
        max_humid = max(year_data, key=lambda x: int(x.max_humidity) if x.max_humidity else 0)
        print("Highest: ",
              str(max_temp_data.max_temp) + " C on " + max_temp_data.pkt.strftime("%B %d"))
        print("Lowest: ",
              str(min_temp_data.min_temp) + " C on " + min_temp_data.pkt.strftime("%B %d"))
        print("Humid: ",
              str(max_humid.max_humidity) + " % on " + max_humid.pkt.strftime("%B %d"))

    def problem_2(self, year_data):
        max_avg_temp = max(year_data, key=lambda x: int(x.mean_temp) if x.mean_temp else -200)
        min_avg_temp = min(year_data, key=lambda x: int(x.mean_temp) if x.mean_temp else 200)
        print("Highest Average: " + max_avg_temp.mean_temp + " C")
        print("Min Average: " + min_avg_temp.mean_temp + " C")
        print("Average Mean Humidity: " + str(self.average_humidity(year_data)) + " %")

    def average_humidity(self, year_data):
        sum_humidity = 0
        for data in year_data:
            if data.mean_humidity:
                sum_humidity = sum_humidity + int(data.mean_humidity)

        return sum_humidity / len(year_data)

    def problem_3(self, year_data):
        print(year_data[0].pkt.strftime('%B %Y'))
        for data in year_data:
            if data.max_temp or data.min_temp:
                print(
                    f"{data.pkt.strftime('%d')} {OKRED}{self.get_plus(int(data.max_temp))} {Default} {data.max_temp} C")
                print(
                    f"{data.pkt.strftime('%d')} {OKBLUE}{self.get_plus(int(data.min_temp))} {Default} {data.min_temp} C")

    def bonus_task(self, year_data):
        print(year_data[0].pkt.strftime('%B %Y'))
        for data in year_data:
            if data.max_temp or data.min_temp:
                print(
                    f"{data.pkt.strftime('%d')} {OKRED}{self.get_plus(int(data.max_temp))}{OKBLUE}{self.get_plus(int(data.min_temp))} {Default} {data.max_temp} -{data.min_temp}C ")

    def get_plus(self, count):
        plus_str = ""
        for i in range(count):
            plus_str += "+"
        return plus_str
