def calculate(a,b,operator):
    if operator == "+":
        result = int(a) + int(b)
    elif operator == "-":
        result = int(a) - int(b)
    elif operator == "*":
        result = int(a) * int(b)
    elif operator == "/":
        result = float(a) / float(b)
    return result


print("Calculator");
count = 0
while count == 0:
    num1 = input("First Number: ")
    option = input("Operator (+, -, *, /, =): ")
    if option == "=":
        print("Results: ", num1)
        break
    num2 = input("Second Number: ")
    results = calculate(num1,num2,option)
    print("Results: ", results)
    count = count + 1
while count > 0:
    option = input("Operator (+, -, *, /, =): ")
    if option == "=":
        print("Results: ", results)
        break
    num2 = input("Second Number: ")
    results = calculate(results, num2, option)
    print("Results: ", results)


