def is_harshad_number(number):
	first_number=number/10
	second_number=number%10
	sum=first_number+second_number
	if number%sum==0:
		print "harshad no. hai"
	else:
		print "not harshad no. "
is_harshad_number(input("enter your no."))

def is_harshad_number(number):
	i=1
	while i<number:
		b=i/10
		c=i%10
		sum=b+c
		if i%sum==0:
			print "harshad no."
		else:
			print "not harshad no."
		i=i+1
is_harshad_number(1000)