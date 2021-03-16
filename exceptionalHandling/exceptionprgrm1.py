no1=int(input("Enter the no1"))
no2=int(input("Enter the no2"))
try:
    res=no1/no2
    print(res)
except Exception as e:
    no2 = int(input("Enter the no2"))
    try:
        res=no1/no2
        print(res)
    except Exception as e:
        print(e.args)

print("data base operation")
print("file write")


