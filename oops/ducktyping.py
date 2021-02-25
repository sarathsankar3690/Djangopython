class Swift:
    def start(self):
        print("swift starts")
    def accelerate(self):
        print("swift accelerates")
    def stops(self):
        print("swift stops")
class Seltos:
    def start(self):
        print("seltos starts")
    def accelerate(self):
        print("seltos accelerates")
    def stops(self):
        print("seltos stops")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.stops()
sw=Swift()
p=Person()
p.drive(sw)


