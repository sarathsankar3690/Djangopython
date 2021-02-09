arr=[10,11,12,13,14,16,14]
element=int(input("Enter the element for search: "))
flg=0
cnt=0
for num in arr:
    if (element==num):
        flg=1
        break
    else:
        flg=0
if flg==1:
    print("element is found!")
if flg==0:
    print("element is not found!")
print(cnt)