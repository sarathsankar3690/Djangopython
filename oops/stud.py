class student:
    def __init__(self,rol,name):
        self.name=name
        self.rol=rol

    def print_stud(self):
        print(self.rol,self.name)
st=student(1001,"ajay")
st.print_stud()