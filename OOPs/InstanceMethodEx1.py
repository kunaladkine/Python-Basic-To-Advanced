#program for demonstrating instance method and self
#InstanceMethodExx1.py

class Student:
    def readstudata(self):
        print("Inside Method: Address of Current Object=",id(self))

#main program
#create two objects of student Object

s1=Student()
print("Main program : Address of s1 object =",id(s1))
s1.readstudata()
print("_"*50)
s2=Student()
print("Main program: Address of s2 object=",id(s2))
s2.readstudata()