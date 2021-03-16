class Employee:
    def __init__(self,id,name,job,salary,experience):
        self.id=id
        self.name=name
        self.job=job
        self.salary=salary
        self.experience=int(experience)

    def __str__(self):
        return self.name
f=open("employeee","r")
employeees=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    job=data[2]
    salary=data[3]
    experience=data[4]
    obj=Employee(id,name,job,salary,experience)
    employeees.append(obj)
print(employeees)
# for high in employeees:
#     print(max(high))

# enames=list(map(lambda emp:emp.salary,employeees))
# print(enames)

# develops=list(filter(lambda desig:desig.job=="Developer",employeees))
# enames=list(map(lambda emp:emp.name,develops))
# print(enames)

explist=list(filter(lambda emp:emp.experience > 2,employeees))
for i in explist:
    if i.experience>2:
        print(i)
# print(explist)

cnt=0
qas=len(list(filter(lambda desig:desig.job=="Qa",employeees)))
print(qas)
# ename=list(map(lambda emp:emp.name,qas))

hisal=max(list(map(lambda emp:emp.salary,employeees)))
print(hisal)













