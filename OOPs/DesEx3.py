import time
from encodings.rot_13 import rot13


class Employee:
    def __init__(self,eno,ename):
        print("I am from Parameterized Constructor")
        self.eno=eno
        self.ename=ename
        print("\tEmp Number:{}".format(self.eno))
        print("\tEmp Name:{}".format(self.ename))
        print("_"*50)
    def __del__(self):
        print("GC Calls __del__() to de-allocate memory space :",id(self))

#main program
print("Program Execution Started")
print("----------------------------------------------------")
eo1=Employee(1,"RS")
time.sleep(3)
print("NO Longer Interested to use eo1 object")
time.sleep(3)
del eo1 #forcefull garbadge collection
eo2=Employee(2,"TS")
time.sleep(3)
print("NO Longer Interested to use eo2 object")
time.sleep(3)
del eo2
eo3=Employee(3,"RS")
time.sleep(3)
print("NO Longer Interested to use eo3 object")
time.sleep(3)
del eo3
time.sleep(3)
print("Program Execution Ended")