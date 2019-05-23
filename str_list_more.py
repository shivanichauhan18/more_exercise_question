sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
i=0
count=0
str_new_list=[]
while i<len(sentence):
    j=i
    word=""
    space=" "
    while j<len(sentence):
        if sentence[j]==space:
            break
        else:
            word=word+sentence[j]
        j=j+1
    str_new_list.append(word)

    i=j+1
print str_new_list
