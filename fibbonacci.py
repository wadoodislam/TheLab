def fibonacci(n):
	seed_val_1 = 0
	seed_val_2 = 1
	for i in range(n):
		seed_val_1, seed_val_2 = seed_val_2, seed_val_1+seed_val_2
		print(seed_val_2)

fibonacci(5)