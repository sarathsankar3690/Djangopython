num=int(input("Enter the number"))
flg=0
for i in range(20,51):
    if (num>20) & (num<50):
        flg=0
        break
    else:
        flg=1
if flg==0:
    print(num, "is with in the limit")
else:
    print(num,"is not with in the limit")

#if num in range(20,50):
   # print("true")
#else:
    #print("false")

