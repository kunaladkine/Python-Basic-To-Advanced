#Syntax : varname={key1:value1,key2:value2,...-key-n:value-n}
#here key1,key2....key-n represents of values of key.
#val1,val2,....val-n represents of values of values.
from time import process_time_ns

#Empty Dict

dicobj={}       #empty dict
print(dicobj)

dictobj1=dict()     #empty dict
print(dictobj1)

#nonempty dict
# dictobj[key1]=val1            adding key,value to empty / nonepty dict

d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
print(d1,type(d1))
d2={"python":1,"C":2,"Java":3,"C++":4}
print(d2,type(d2))

print(len(d1))

#----------------
d3={10:1.2,10:2.3,10:4.5,10:0.2}        #updated value will be taken
print(d3)

d4={10:1.2,20:2.3,10:1.9,80:2.9}        #updated value will be taken
print(d4)

#-------------
d5={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
print(d5,type(d5))

# print(d5[0])      #get the keyvalue error because no indexing
print(d5[10])
print(d5[20])
print(d5[30])
print(d5[40])

d5[10]="Guava"      #value will be updated using key
print(d5)

#Inserted Entry
d6={}       #empty dict
print(len(d6))
d6[100]=1.2
d6[200]=2.2
d6[300]=1.2
d6[400]=4.2
print(d6)       #after updation