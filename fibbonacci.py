def fibonacci(limit, seed_val_1=0, seed_val_2=1):
	for i in range(limit):
		seed_val_1, seed_val_2 = seed_val_2, seed_val_1+seed_val_2
		print(seed_val_2)


seed_val_1= int(input("Enter 1st seed value: "))
seed_val_2= int(input("Enter 2nd seed value: "))
limit = int(input("Enter limit: "))





fibonacci(limit,seed_val_1, seed_val_2)


