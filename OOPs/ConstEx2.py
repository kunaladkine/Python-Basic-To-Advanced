#demonstrating on Parameterized Constructor
#ConstEx2.py

class Student:
    def __init__(self,name,age):        #parameterized constructor
        self.name=name
        self.age=age
        print("\tEmployee Name=",self.name)
        print("\tEmploye age=",self.age)

#main program
s1=Student("Kunal",32)          #Object Creation--Makes the PVM to call Parameterized Constructor
s2=Student("amol",23)           #Object Creation--Makes the PVM to call Parameterized Constructor