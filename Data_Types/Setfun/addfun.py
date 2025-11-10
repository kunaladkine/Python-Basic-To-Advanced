#add()
#Syntax : Setobj.add(value)
#this function is used for adding the any type of value to set object.

s1={10,"Travis",3+4j}
print(s1,type(s1),id(s1))
s1.add("PYTHON")
print(s1,id(s1))
s1.add(True)
print(s1)
s1.add(100)
print(s1)

s1=[100]    #typeerror: 'set' object does not support item assignment
