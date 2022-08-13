def fibonacci(nth, first=0, second=1):
    for i in range(nth):
        print(first)
        first, second = second, first + second


fibonacci(5)
