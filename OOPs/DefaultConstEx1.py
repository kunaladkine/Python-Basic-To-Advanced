#Demosntrating on Default Constructor
#DefaultConstEx1.py

class Student:
    def __init__(self):
        print("I am from default constructor")
        self.name="Kunal"
        self.age=23
        print("\tStudent Name {}".format(self.name))
        print("\tStudent Age {}".format(self.age))

#main program
t1=Student()        #Object Creation--Makes the PVM to call Parameterized Constructor
t2=Student()
t3=Student()