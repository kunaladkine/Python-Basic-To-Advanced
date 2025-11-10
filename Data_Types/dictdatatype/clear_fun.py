#Syntax : dictobj.clear()
#this function is used for removing all the values from mdict object.
#when we call this function on empty dict object then we get space Or None as result.

d1={10:1.2,20:2.2,30:3.3,40:4.4}
print(d1,type(d1),id(d1))
print(len(d1))

d1.clear()
print(d1,type(d1),id(d1))
print(len(d1))
print(d1.clear())       #it gives None , an Empty dict

print({}.clear())       #it gives None, 