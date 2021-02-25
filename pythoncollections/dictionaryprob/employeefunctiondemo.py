employees={
    1000:{"eid":1000,"ename":"ram","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"sreerag","desig":"tester","salary":20000},
    1002:{"eid":1002,"ename":"amit","desig":"trainee","salary":15000}
}

def print_emp_details(**kwargs):  #kwargs={eid:1000,property:salary}
    id=kwargs["eid"] #1000
    if id in employees:
        print(employees[id]["ename"])
        if "property" in kwargs:
            prop = kwargs["property"]
            print(employees[id][prop])
        else:
            pass

print_emp_details(eid=1000)

