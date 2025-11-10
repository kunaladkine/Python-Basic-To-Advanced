#program for string sno,sname and marks by ussing classes and object

class Student:pass

#main program
#create two objects of student
s1=Student()
s2=Student()
print("ID of s1=",id(s1))
print("ID of s2=",id(s2))
print("Initial Content of s1 object=",s1.__dict__)
print("Initial Content of s2 object=",s2.__dict__)
print("Intially, Number of Values in s1 object=",len(s1.__dict__))
print("Intially, Number of Values in s2 object=",len(s2.__dict__))
print("_"*50)
#place the instance data members in s1 object
#Place the Instance Data members in s1 Object.
s1.sno=10
s1.sname="RS"
s1.marks=44.55 # here sno,sname and marks are called Instance Data Members
#Place the Instance Data members in s2 Object.
s2.stno=20
s2.sname="TR"
s2.marks=66.66  # here stno,sname and marks are called Instance Data Members
s2.cname="JNTU(H)"
#Display the Content of s1 Object
print("---------------------------------------------------------")
print("First Object s1 Data ")
print("Initial Content of s1 object")
print(s1.__dict__)
print("Initially,Number of Values in s1 object=",len(s1.__dict__))
print("------------------------------------------------------------")
#Display the Content of s2 Object
print("Second Object s2 Data ")
print("Initial Content of s2 object")
print(s2.__dict__)
print("Initially,Number of Values in s2 object=",len(s2.__dict__))
print("----------------------------------------------------------")