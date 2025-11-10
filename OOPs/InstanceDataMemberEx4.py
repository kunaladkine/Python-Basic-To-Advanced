#program for adding of Two Numbers by using Class and Objects
#InstanceDataMembersEx5.py
class Sum:pass

#main Program
s1=Sum()
s1.a=float(input("Enter First value:"))
s1.b=float(input("Enter Second value:"))
s1.c=s1.a+s1.b
print("sum({},{})={}".format(s1.a,s1.b,s1.c))