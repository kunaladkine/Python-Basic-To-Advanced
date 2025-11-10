#Syntax DictObj.popitem()
#this function is used for removing last (Key,Value) from dict object.
#when we call this function on empty dict object then we get KeyError.

d1={10:1.2,20:2.2,30:3.3,40:4.4}
print(d1,type(d1))

d1.popitem()        #last item is removed
print(d1)

d1.popitem()
print(d1)

print({}.popitem())     #KeyError


