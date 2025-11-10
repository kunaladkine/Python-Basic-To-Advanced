#program for String sno,sname and marks by using Classes and Object
#InstanceDataMembersEx3.py
class Student:pass

#Main Program
#Create Two objects of student.
s1=Student()
s2=Student()
print("ID of s1=",id(s1))
print("ID of s2=",id(s2))
print("Initial Content of s1 object=",s1.__dict__)
print("Initial Content of s2 object=",s2.__dict__)
print("Initially,Number of Values in s1 object=",len(s1.__dict__))
print("Initially,Number of Values in s2 object=",len(s2.__dict__))
print("---------------------------------------------------------")
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
for dmn,dmv in s1.__dict__.items():
    print("\t{}--->{}".format(dmn,dmv))
print("------------------------------------------------------------")
#Display the Content of s2 Object
print("Second Object s2 Data ")
for dmn in s2.__dict__:
    print("\t{}--->{}".format(dmn,s2.__dict__[dmn]))
print("----------------------------------------------------------")