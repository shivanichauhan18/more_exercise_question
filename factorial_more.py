def factorial(number):
	i=1
	sum=1
	while i<=number:
		sum=sum*i
		i=i+1
	return sum
print factorial(7)