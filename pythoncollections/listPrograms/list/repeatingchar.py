# pattern="ABBC"
# flg=0
# for char in pattern:
#     if pattern.count(char)>1:
#         flg=1
#         print(char)
#         break


pattern="ABBA"
flg=0
for i in pattern:
    print(i)
    for j in range(0,len(pattern)-1):
        if i==j:
            flg=1
            print(i)
            break
if flg==0:
    print("not found")


