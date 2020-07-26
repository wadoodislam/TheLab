def add(a, b):
    return int(a) + int(b)
def subtract(a, b):
    return int(a) - int(b)
def multiply(a, b):
    return int(a) * int(b)
def divide(a, b):
    return float(a) / float(b)

print("Calculator");
num1 = input("First Number: ")
option = input("Operator (+, -, *, /): ")
num2 = input("Second Number: ")
if option == "+":
        result = add(num1,num2)
elif option == "-":
        result =  subtract(num1,num2)
elif option == "*":
        result = multiply(num1,num2)
elif option == "/":
        result = divide(num1,num2)
print("Results: ",result)

