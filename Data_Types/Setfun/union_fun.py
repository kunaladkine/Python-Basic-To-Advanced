#Syntax : - SetObj3=SetObj1.union(SetObj2)
#this Function obtains all the Unique Elements of SetObj and setObj2 and place the Resultant Elements in setobj3

#Ex1

s1={10,20,30}
s2={10,20,40,50}
print(s1,type(s1),id(s1))
print(s2,type(s2),id(s2))


s3=s1.union(s2)
print(s3)

s4=s1.union(s2,{10,"a","e","i","o","u"})
print(s4)

