import time
class Employee:
    def __init__(self,eno,ename):
        print("I am from Parameterized Constructor",id(self))
        self.eno=eno
        self.ename=ename
        print("\tEmp Number ={}".format(self.eno))
        print("\tEmp Name ={}".format(self.ename))
        print("_"*50)

    def __del__(self):
        print("GC Calls __del__() to de-allocate memory space :",id(self))

#Main Program
print("Program Execution Started")
print("----------------------------------------------------")
eo1=Employee(100,"RS")
eo2=Employee(200,"TR")
eo3=Employee(200,"TR")
print("Program Execution Ended")
time.sleep(5)