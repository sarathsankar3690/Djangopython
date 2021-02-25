class Grandparents:
    def m1(self):
        print("Inside m1")
class parent(Grandparents):
    def m2(self):
        print("inside m2 ")
class child(parent):
    def m3(self):
        print("inside m3")

ch=child()
ch.m3()
ch.m2()
ch.m1()

