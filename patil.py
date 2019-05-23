user_input=raw_input("enter the operation ")
def add_numbers(number_x, number_y,operation):
	if operation=="addition":
		addition= number_x + number_y
    	return addition
	if operation=="sabtraction":
		subtraction=number_x-number_y
		return subtraction
	if operation=="multiplication":    
		multiplication=number_x*number_y
		return multiplication
	if operation=="division":
		division=number_x/number_y
		return division
	if operation=="modulus":
		modulus=number_x%number_y
  		return modulus
print add_numbers(4,5,user_input)