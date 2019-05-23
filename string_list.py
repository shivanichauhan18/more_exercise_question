string=["rishabh","abhisek","rishabh","divya","abhisek","divya","shivani"]
i=0
new_list=[]
while i<len(string):
	j=1
	while j<len(string):
		if string[i]==string[j]:
			if string[j] not in  new_list:
				new_list.append(string[j])		
		j=j+1
	i=i+1
print new_list