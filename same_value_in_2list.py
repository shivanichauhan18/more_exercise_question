def same_number(list1,list2):
	i=0
	new_list=[]
	while i<len(list1):
		j=0
		while j<len(list2):
			if list1[i] == list2[j]:
				new_list.append(list1[i])
			j=j+1
		i=i+1
	return new_list
print same_number([1,342,75,23,98],[75,23,98,12,78,10,1])