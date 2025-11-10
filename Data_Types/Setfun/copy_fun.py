#Syntaxx : SetObj2=SetObj1.copy()
#this function is used for copying the content of SetObj1 into setboj2 (Implements shallow copy)

s1={10,20,30}
print(s1,id(s1))
s2=s1.copy()
print(s2,id(s2))

#---------------
s1.add(100)
s2.add("PY")
print(s1,id(s1))
print(s2,id(s2))

s2=s1.copy()
print(s2)

