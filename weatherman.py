import argparse
from datetime import datetime

from WeathermanReporter import WeatherReporter


def parse_date(arg):
    sliced = str(arg).split('/')
    return str(sliced[0]), datetime.strptime(str(sliced[1]), '%m').strftime("%b")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Pass an year value")
    parser.add_argument("-e", help="Pass an year value")
    parser.add_argument("-a", help="Pass an year value")
    parser.add_argument("-c", help="Pass an year value")
    parser.add_argument("-b", help="Pass an year value")
    args = parser.parse_args()

    try:

        if args.e:
            WeatherReporter(args.dir, args.e).problem_1()

        if args.a:
            year, month = parse_date(args.a)
            WeatherReporter(args.dir, year, month).problem_2()

        if args.c:
            year, month = parse_date(args.c)
            WeatherReporter(args.dir, year, month).problem_3()

        if args.b:
            year, month = parse_date(args.b)
            WeatherReporter(args.dir, year, month).bonus_task()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
