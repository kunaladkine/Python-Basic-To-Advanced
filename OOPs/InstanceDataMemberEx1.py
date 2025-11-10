#InstanceDataMemberEx1.py

class Student:pass

s1=Student()
s2=Student()

#main program
s1.sno=12
s1.sname="RS"
s1.ssal=33.44
print("_"*50)
print("First Student Data")
print("\tStudent Name=",s1.sname)
print("\tStudent No=",s1.sno)
print("\tStudent Salary=",s1.ssal)
print("_"*50)
s2.sno=13
s2.sname="TS"
s2.ssal=55.55
print("Second Student Data")
print("\tStudent No=",s2.sno)
print("\tStudent Name=",s2.sname)
print("\tStudent Salary=",s2.ssal)