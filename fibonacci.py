def fibonacci(nth, first, second):


    print(second)
    for i in range(nth):

        # sum = value+value2
        # value2 = value
        # value = sum
        first, second = second, first + second
        print(second)


fibonacci(6, 0, 1)



