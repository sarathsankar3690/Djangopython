n=50
i=1
etotal=0
ototal=0
while (i<=n):
    if (i%2==0):
        etotal=etotal+i
        i+=1
    else:
        ototal=ototal+i
        i+=1

print(etotal)
print(ototal)

