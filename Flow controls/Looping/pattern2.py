# lower=int(input("enter lower limit: "))
# upper=int(input("enter upper limit: "))
# n=int(input("enter power: "))
# for i in range(1,upper+1):
#         if (n<=upper):
#             result=(i**n)
#             print(result)
#         else:
#             break

num=int(input("enter the num: "))
lower=int(input("enter the lower limit: "))
upper=int(input("enter the upper limit: "))
for i in range(1,(upper+1)):
     if i**num in range(lower,(upper+1)):
         print(i**num)




