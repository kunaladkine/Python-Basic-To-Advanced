#GCEX2.py
import sys,time,gc
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Constructor: ",id(self))
		self.eno=eno
		self.ename=ename
		print("\tEmp Number:{}".format(self.eno))
		print("\tEmp Name:{}".format(self.ename))
		print("----------------------------------------------------")
	def __del__(self):
		print("GC Calls __del__() to de-allocate memory space: ",id(self))
		global totmemsp
		totmemsp=totmemsp-sys.getsizeof(self)
		print("\tNow Available Memory space=",totmemsp)

#Main Program
print("Program Execution Started")
print("Initially, Is GC Running=",gc.isenabled())
print("----------------------------------------------------")
eo1=Employee(100,"RS")
eo2=Employee(200,"TR")
eo3=Employee(200,"TR")
gc.disable()
print("Now, Is GC Running=",gc.isenabled())
totmemsp=sys.getsizeof(eo1)+sys.getsizeof(eo2)+sys.getsizeof(eo3)
print("TOTAL MEMORY SPACE=",totmemsp) # 144
print("Program Execution Ended")
time.sleep(5)