class Student:
    def set_student(self,rollno,name,total):
        self.rollno=rollno
        self.name=name
        self.total=total
    def print_student(self):
        print(self.rollno)
        print(self.name)
        print(self.total)
obj=Student()
obj.set_student(10,"Sarath",100)
obj.print_student()