#Demonstrating on Default and Parametrized Constructor

class Student():
    def __init__(self,a=22,b=22):
        print("\tI am From Default / Parameterized Constructor")
        self.a=a
        self.b=b
        print("\tStudent Name:{}".format(self.a))
        print("\tStudent Age:{}".format(self.b))

#main program
t1=Student()
t2=Student(10,23)
t3=Student(a=22,b=34)

'''
#DefaultParameterizedConstEx1.py
class Test:
    def __init__(self,a=10,b=20):
        print("I am from Default / Parameterized Constructor")
        self.a=a
        self.b=b
        print("\tValue of a={}".format(self.a))
        print("\tValue of b={}".format(self.b))

#Main Program
t1=Test() #  Object Creation--Makes the PVM to call Default Constructor
t2=Test(100,200) #  Object Creation--Makes the PVM to call Parameterized Constructor
t3=Test(1000,2000) #  Object Creation--Makes the PVM to call Parameterized Constructor
t4=Test(b=1,a=2) #  Object Creation--Makes the PVM to call Parameterized Constructor
t5=Test(b=500) #  Object Creation--Makes the PVM to call Parameterized Constructor
'''