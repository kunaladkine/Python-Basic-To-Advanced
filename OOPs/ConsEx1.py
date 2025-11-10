#demosntrating on Default or parameter Constructor
#ConstEx1.py
class Student:
    def __init__(self):
        print("\tI Am From Default Constructor")
        self.name="Student"
        self.age=18
        print("\tEmployee No=",self.name)
        print("\tEmploye Age:",self.age)


s1=Student()
s2=Student()

