arr=[10,11,12,13,14,15,16,17,18,19,20]
element=int(input("Enter the search value: "))
arr.sort()
lower=0
upper=len(arr)-1
flg=0
while (lower<=upper):
    mid=(upper+lower)//2
    if (element>arr[mid]):
        lower=mid+1
    elif (element<arr[mid]):
        upper=mid-1
    elif (element==arr[mid]):
        flg=1
        break
if flg==0:
    print("element not found")
elif flg==1:
    print("element is found")

