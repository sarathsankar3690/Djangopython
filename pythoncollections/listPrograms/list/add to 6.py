lst=[1,2,3,4]
n=len(lst)
sum=6
for i in range(0,n):
    for j in range(i,n):
        if (lst[i] + lst[j]==sum):
            print("(",lst[i],",",lst[j],")")