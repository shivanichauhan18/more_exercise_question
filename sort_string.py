name_list=["dog","fox","pig","bafellow","cat"]
i=0
new_list=[]
while i<len(name_list):
	j=0
	while j<len(name_list):
		if name_list[i][j]>name_list[i][j]:
			new_list.append(name_list[j])
		j=j+1
	i=i+1
print new_list