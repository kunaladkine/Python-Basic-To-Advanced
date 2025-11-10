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

#Main Program
print("Program Execution Started")
print("----------------------------------------------------")
eo1=Employee(100,"RS")
eo2=eo1
eo3=eo1 # here eo1,eo2 and eo3 are in Deep Copy
time.sleep(3)
print("No Longer Interested to use eo1 object")
time.sleep(3)
del eo1 # GC will not call Destructor forcefully bcoz still eo2 and eo3 points to memory space
time.sleep(3)
print("No Longer Interested to use eo2 object")
time.sleep(3)
del eo2 # GC will not call Destructor forcefully bcoz still eo3 points to memory space
time.sleep(3)
print("No Longer Interested to use eo3 object")
time.sleep(3)
del eo3
time.sleep(3)
print("Program Execution Ended")