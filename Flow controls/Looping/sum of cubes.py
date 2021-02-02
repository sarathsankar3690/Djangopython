n=int(input("Enter the digits: "))
digits=0
sum=0
while (n!=0):
    digits=n%10
    sum+=digits**3
    n=n//10
print(sum)


