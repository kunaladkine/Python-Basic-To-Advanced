#Demonstrating on Parametrized Constructor
#parameterizedcontex1.py

class Test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("\tStudent Name: {}".format(self.name))
        print("\tStudent Age:".format(self.age))

#main program
t1=Test("kunal",23)
t2=Test("Jarvis",33)