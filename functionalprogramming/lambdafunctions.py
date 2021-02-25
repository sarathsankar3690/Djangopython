# add = lambda num1,num2:num1+num2
# print(add(10,20))
#
# sub = lambda num1,num2:num1-num2
# print(sub(30,20))
#
# mul = lambda num1,num2:num1*num2
# print(mul(6,5))
#
# div = lambda num1,num2:num1/num2
# print(div(60,20))
#
# cube = lambda num1:num1**3
# print(cube(4))
#
lst=[1,2,3,4,5,6,7,8,9]
# lambda num:num**2
# print(list(map(lambda num:num**2,lst)))
# #
# lambda num:num%2==0
# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)

num=list(filter(lambda num:num>3,lst))
print(num)

# names=["ram","raju","ravi"]
# upp_name=lambda nam:nam.upper()
# # print(list(map(lambda nam:nam.upper(),names)))
# print(list(map(upp_name,names)))





