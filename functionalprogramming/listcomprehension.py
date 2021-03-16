lst1=[1,2,3]
lst2=[3,4,5]
# lst=[]
# for i in lst1:
#     for j in lst2:
#         lst.append((i,j))
# print(lst)

# op=[i**2 for i in lst1]
# print(op)

opp=[i for i in lst1 for j in lst2 if i==j]
print(opp)

high=[j for j in lst2 if max(lst2)]
print(high)
# same=[(i,j) if i==j]
# print(same)