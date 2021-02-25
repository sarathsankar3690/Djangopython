class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
P1=Person(16,"ajay")
P2=Person(42,"varun")
P3=Person(78,"Harrish")
lst=[]
lst.append(P1)
lst.append(P2)
lst.append(P3)
high=[]
for i in lst:
    high.append(i.age)
m=max(high)
for i in lst:
    if m==i.age:
        print(i.name,i.age)




