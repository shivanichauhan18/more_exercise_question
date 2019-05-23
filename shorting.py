def string(list_A,list_B):
    i=0
    j=0
    new_list=[]
    while i<len(list_A) and j<len(list_B):
        if list_A[i]<=list_B[j]:
            if list_A[i] not in new_list:        
                new_list.append(list_A[i])
            i=i+1
        else:
            if list_B[j] not in new_list:
                new_list.append(list_B[j])
            j=j+1
    print  new_list
string([1,5,10,12,15,16],[1,2,10,13,16])

