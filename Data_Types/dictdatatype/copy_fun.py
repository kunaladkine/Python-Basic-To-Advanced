#Syntax : dictobj2=dictobj1.copy()

#this function is used for copyinng the content of dictobj1 into another dictobj2 (Implementns shallow Copy)

d1={10:1.2,20:2.2,30:3.3,40:4.4}
print(d1,type(d1),id(d1))

d2=d1.copy()
print(d2,type(d1),id(d1))

d1[10]=3.3
d2[40]=1.3
print(d1,type(d1),id(d1))
print(d2,type(d2),id(d2))

