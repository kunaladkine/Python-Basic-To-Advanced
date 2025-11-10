import sys,time
class Employee:
    def __init__(self,eno,ename):
        print(" I am From parameterized constructor:",id(self))
        self.eno=eno
        self.ename=ename
        print("\tEMployee No:{}".format(self.eno))
        print("\tEmplpyee Name:{}".format(self.ename))
        print("_"*50)

    def __del__(self):
        print("GC Calls __del__() to de-allocate memory space :",id(self))
        global totmemsp
        totmemsp=totmemsp-sys.getsizeof(self)
        print("\tNow Available Memory Space=",totmemsp)

#main program
print("Program Execution Started")
print("_"*50)
eo1=Employee(100,'TS')
eo2=Employee(200,"TR")
totmemsp=sys.getsizeof(eo1)+sys.getsizeof(eo2)
print("Total Memory Space=",totmemsp)
print("Program Execution Started")
time.sleep(5)
