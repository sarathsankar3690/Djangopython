age=int(input("Enter the age: "))
try:
    if age<0:
        raise Exception("invalid age!")
    else:
        print("valid")
except Exception as e:
    age = int(input("Enter the age: "))
    try:
        if age>0:
            print("valid")
    except Exception as e:
        print("invalid")
        print(e.args)
finally:
    print("data base operation")
    print("file write")