from typing import List

import WeatherManFileHandle
import WeatherManComputations
from datetime import datetime
import argparse

OKBLUE = '\033[34m'
OKRED = '\033[31m'
Default = "\033[39m"


def problem_1(year_data):
    max_temp_data = max(year_data, key=lambda x: int(x.max_temp) if x.max_temp else -200)
    min_temp_data = min(year_data, key=lambda x: int(x.min_temp) if x.min_temp else 200)
    max_humid = max(year_data, key=lambda x: int(x.max_humidity) if x.max_humidity else 0)
    print("Highest: ",
          max_temp_data.max_temp + " C on " + datetime.strptime(max_temp_data.pkt, '%Y-%m-%d').strftime("%B %d"))
    print("Lowest: ",
          min_temp_data.min_temp + " C on " + datetime.strptime(min_temp_data.pkt, '%Y-%m-%d').strftime("%B %d"))
    print("Humid: ", max_humid.max_humidity + " % on " + datetime.strptime(max_humid.pkt, '%Y-%m-%d').strftime("%B %d"))


def problem_2(year_data):
    max_avg_temp = max(year_data, key=lambda x: int(x.mean_temp) if x.mean_temp else -200)
    min_avg_temp = min(year_data, key=lambda x: int(x.mean_temp) if x.mean_temp else 200)
    print("Highest Average: " + max_avg_temp.mean_temp + " C")
    print("Min Average: " + min_avg_temp.mean_temp + " C")
    print("Average Mean Humidity: " + str(average_humidity(year_data)) + " %")


def average_humidity(year_data):
    sum_humidity = 0
    for data in year_data:
        if data.mean_humidity:
            sum_humidity = sum_humidity + int(data.mean_humidity)

    return sum_humidity / len(year_data)


def problem_3(year_data):
    print(datetime.strptime(year_data[0].pkt, '%Y-%m-%d').strftime('%B %Y'))
    for data in year_data:
        if data.max_temp or data.min_temp:
            print(
                f"{datetime.strptime(data.pkt, '%Y-%m-%d').strftime('%d')} {OKRED}{get_plus(int(data.max_temp))} {Default} {data.max_temp} C")
            print(
                f"{datetime.strptime(data.pkt, '%Y-%m-%d').strftime('%d')} {OKBLUE}{get_plus(int(data.min_temp))} {Default} {data.min_temp} C")


def bonus_task(year_data):
    print(datetime.strptime(year_data[0].pkt, '%Y-%m-%d').strftime('%B %Y'))
    for data in year_data:
        if data.max_temp or data.min_temp:
            print(
                f"{datetime.strptime(data.pkt, '%Y-%m-%d').strftime('%d')} {OKRED}{get_plus(int(data.max_temp))}{OKBLUE}{get_plus(int(data.min_temp))} {Default} {data.max_temp} -{data.min_temp}C ")


def get_plus(count):
    plus_str = ""
    for i in range(count):
        plus_str += "+"
    return plus_str


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Pass an year value")
    parser.add_argument("-e", help="Pass an year value")
    parser.add_argument("-a", help="Pass an year value")
    parser.add_argument("-c", help="Pass an year value")
    parser.add_argument("-b", help="Pass an year value")
    args = parser.parse_args()
    computations = WeatherManComputations.Computations(args.dir + "/*.txt")
    if args.e:
        if 2004 <= int(args.e) <= 2016:
            problem_1(computations.get_data_for_year(args.e))
        else:
            print("Invalid Entry for year")
    if args.a:
        sliced = str(args.a).split('/')
        problem_2(computations.get_data_for_month(int(sliced[0]), int(sliced[1])))
    if args.c:
        sliced = str(args.c).split('/')
        problem_3(computations.get_data_for_month(int(sliced[0]), int(sliced[1])))
    if args.b:
        sliced = str(args.b).split('/')
        bonus_task(computations.get_data_for_month(int(sliced[0]), int(sliced[1])))


if __name__ == "__main__":
    main()
