class Maths:
    def add(self):
        print("inside no argmath method")
    def add(self,num1,num2):
        print("inside single arg method")
    def add(self,num1):
        print("inside double arg method")
math=Maths()
math.add(10,20)