def add(a, b):
    return int(a) + int(b)
def subtract(a, b):
    return int(a) - int(b)
def multiply(a, b):
    return int(a) * int(b)
def divide(a, b):
    return int(a) / int(b)

print("Select Operation:\n1- Add,\n2- Subtract,\n3- Multiply,\n4- Divide.")
option = int(input("Enter you choice from 1/2/3/4 :- "))
num1 = input("Enter your first number :- ")
num2 = input("Enter your second number :- ")
if option == 1:
        print("results : ", add(num1,num2))

elif option == 2:
        print("results : ", subtract(num1,num2))

elif option == 3:
        print("results : ", multiply(num1,num2))

elif option == 4:
        print("results : ", divide(num1,num2))

