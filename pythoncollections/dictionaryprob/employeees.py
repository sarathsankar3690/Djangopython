employees={
    1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"sreerag","desig":"tester","salary":20000},
    1002:{"eid":1002,"ename":"amit","desig":"trainee","salary":15000}
}
eid=int(input("Enter the eid: "))
property= input("Enter the property: ")
if eid in employees:
    print(employees[eid]["ename"],employees[eid]["desig"])
    if property in employees[eid]:
        print(employees[eid][property])
    else:
        print("Invalid input")
else:
    print("invalid input")
