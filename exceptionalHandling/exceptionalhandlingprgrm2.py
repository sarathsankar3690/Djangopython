lst=[10,20,30]
pos=int(input("Give position: "))
try:
    print(lst[pos])
except Exception as e:
    print(e.args)

print("data base operation")
print("file write")