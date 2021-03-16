# lst=[3,4,2,6,7,8]
# #if(no>5):
# #   no+1
# #else:
# #   no-1
#
# data=[ num+1 if num>5 else num-1 for num in lst]
# print(data)

lst=[[10,20],[30,40],[40,50],[50,60]]
data=[i for n in lst for i in n]
print(data)