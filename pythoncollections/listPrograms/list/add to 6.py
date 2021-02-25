lst=[1,2,3,4]
# n=len(lst)
# sum=6
# for i in range(0,n):
#     for j in range(i,n):
#         if (lst[i] + lst[j]==sum):
#             print("(",lst[i],",",lst[j],")")
sum=6
low=0
upp=len(lst)-1
cnt=0
while (low<upp):
    total=lst[low]+lst[upp]
    if total==sum:
        print(lst[low],lst[upp])
        low+=1
        upp-=1
        break
    elif total>sum:
        upp-=1         #index value of upper number will reduced
    elif total<sum:
        low+=1
        cnt+=1

