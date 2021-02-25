class Employee:
    company_name="ctc"

    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):
        return str(self.age)+self.name

emp1=Employee(25,"Ram")
emp2=Employee(27,"Deepu")
emp3=Employee(30,"Das")
lst=[]
lst.append(emp1)
lst.append(emp2)
lst.append(emp3)

print(emp3)