def divide_two_numbers(x,y):
	if y == 0:
		raise ValueError('Cannot divide by zero')
	return x / y

print divide_two_numbers(5,2)