print("Select Operation:\n1- Add,\n2- Subtract,\n3- Multiply,\n4- Divide.");
option = int(input("Enter you choice from 1/2/3/4 :- "));
num1 = input("Enter your first number :- ");
num2 = input("Enter your second number :- ");
if option == 1:
    {
        print("results : ", int(num2)+int(num1))
    }
elif option == 2:
    {
        print("results : ", int(num1)-int(num2))
    }
elif option == 3:
    {
        print("results : ", int(num1)*int(num2))
    }
elif option == 4:
    {
        print("results : ", int(num1) / int(num2))
    }
