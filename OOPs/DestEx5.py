import time
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Constructor:")
		self.eno=eno
		self.ename=ename
		print("\tEmp Number:{}".format(self.eno))
		print("\tEmp Name:{}".format(self.ename))
		print("----------------------------------------------------")
	def __del__(self):
		print("GC Calls __del__() to de-allocate memory space: ")

#main program
print("Program Execution")
print("_"*50)
eo1=Employee(1,"TS")
eo2=eo1
eo3=eo1     #here eo1,eo2 and eo3 are in deep copy
print("_"*50)
