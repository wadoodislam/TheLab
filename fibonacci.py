def fibonacci(nth, first=0, second=1):

    print(second)
    for i in range(nth):
        first, second = second, first + second
        print(second)


fibonacci(5)
