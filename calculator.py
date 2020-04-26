def calculator(result, op, num2):
	if op == "+":
		result = result + num2 
	elif op == "-":
		result = result - num2
	elif op == "/":
		result = result / num2
	elif op == "*":
		result = result * num2
	return result

if __name__=="__main__":
	op= "2"
	result = float(input("Enter number 1"))

	while op!="q":
		op = input("Enter operator")
		if op != "=" and op!="q":
			num2 = float(input("Enter number 2"))
			result = calculator(result, op, num2)
		else:
			print(result)
