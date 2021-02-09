lst=[21,22,26,28,29,32,37]
new_list=[]
while lst:
    low=lst[0]
    for i in lst:
        if i<low:
            low=i
    new_list.append(low)
    lst.remove(low)
print(new_list)
