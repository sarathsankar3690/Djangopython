n=int(input("enter the number: "))
pattern=""
sum=0
for i in range (1,(n+1)):
        pattern=str(n)*i
        print(pattern)
        sum=sum+int(pattern)
print("sum is ",sum)





