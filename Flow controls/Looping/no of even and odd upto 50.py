limit=int(input("Enter the limit"))
i=1
oddsum=0
evensum=0
ecount=0
ocount=0
while (i<=limit):
    if(i%2==0):
        evensum+=1
        ecount+=1
    else:
        oddsum+=1
        ocount+=1
print(evensum)
print(ecount)


