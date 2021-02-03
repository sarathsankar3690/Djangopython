n=int(input("Enter the number: "))
flg=0
for i in range(2,n):
    if (n%10==0):
        flg=1
        break
    else:
        flg=0
if (flg==0):
    print("prime number")
else:
    print("not prime number")