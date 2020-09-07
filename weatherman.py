import argparse
from datetime import datetime

from WeatherRegister import WeatherRegister
from WeathermanReporter import WeatherReporter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Pass an year value")
    parser.add_argument("-e", help="Pass an year value")
    parser.add_argument("-a", help="Pass an year value")
    parser.add_argument("-c", help="Pass an year value")
    parser.add_argument("-b", help="Pass an year value")
    args = parser.parse_args()

    if args.e:
        if 2004 <= int(args.e) <= 2016:
            computations = WeatherRegister(args.dir + "/Murree_weather_" + str(args.e) + "_" + "*.txt")
            WeatherReporter().problem_1(year_data=computations.data_list)
        else:
            print("Invalid Entry for year")
    if args.a:
        sliced = str(args.a).split('/')
        computations = WeatherRegister(
            args.dir + "/Murree_weather_" + str(sliced[0]) + "_" + datetime.strptime(str(sliced[1]), '%m').strftime(
                "%B")[:3] + ".txt")
        WeatherReporter().problem_2(year_data=computations.data_list)
    if args.c:
        sliced = str(args.c).split('/')
        computations = WeatherRegister(
            args.dir + "/Murree_weather_" + str(sliced[0]) + "_" + datetime.strptime(str(sliced[1]), '%m').strftime(
                "%B")[:3] + ".txt")
        WeatherReporter().problem_3(year_data=computations.data_list)
    if args.b:
        sliced = str(args.b).split('/')
        computations = WeatherRegister(
            args.dir + "/Murree_weather_" + str(sliced[0]) + "_" + datetime.strptime(str(sliced[1]), '%m').strftime(
                "%B")[:3] + ".txt")
        WeatherReporter().bonus_task(year_data=computations.data_list)


if __name__ == "__main__":
    main()
