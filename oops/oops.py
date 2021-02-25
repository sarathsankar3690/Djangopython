class Person:
    def set_person(self,age,name):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name)
        print(self.age)

obj=Person()
obj.set_person(25,"ram")
obj.print_person()
