def divide_two_numbers(x,y):
	#Raise exception to avoid a divide-by-zero
	if y == 0:
		raise ValueError('Cannot divide by zero')

	return float(x) / float(y)



