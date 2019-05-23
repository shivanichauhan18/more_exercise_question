def factorial(number):
	sum=1
	while number>0:
		sum=number*sum
		number=number-1
	return sum
print factorial(input("enter your factorial_no."))