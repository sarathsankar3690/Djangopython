class Employee:
    def __init__(self,id,name,job,salary,experience):
        self.id=id
        self.name=name
        self.job=job
        self.salary=salary
        self.experience=experience

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
# for high in employeees:
#     print(max(high))

enames=list(map(lambda emp:emp.salary,employeees))
print(enames)






