#Syntax : DictObj.pop(Key)
#this function is used for removing the (Key,value from dict object by passing the values of key.
#if the value of key does not exist then we get keyerror.

d1={10:1.2,20:2.2,30:3.3,40:4.4}
print(d1,type(d1),id(d1))

d1.pop(10)      #key 10 and its value removed
print(d1)

d1.pop(30)      #key 30 an its value removed
print(d1)

print({}.pop(30))       #keyerror get if we give another key that not present in
print(dict().pop(20))     #keyerror
