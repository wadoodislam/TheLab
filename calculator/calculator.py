def calculate(a,b,operator):
    if operator == "+":
        result = float(a) + float(b)
    elif operator == "-":
        result = float(a) - float(b)
    elif operator == "*":
        result = float(a) * float(b)
    elif operator == "/":
        result = float(a) / float(b)
    return result

print("Calculator");
num1 = input("First Number: ")
option = "+"
results = num1;
while option != "=":
    option = input("Operator (+, -, *, /, =): ")
    if option == "=":
        print("Results: ", results)
        break
    num2 = input("Second Number: ")
    results = calculate(results, num2, option)
    print("Results: ", results)


