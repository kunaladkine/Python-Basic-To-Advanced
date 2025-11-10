#syntax : varname=DictObj.items()
#this function is used for obtaining (key,value) place the (key,values)in LHS Varname and whose Type is < class 'dict_items'>

d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1)

kvs=d1.items()
print(kvs,type(kvs))
#-------------------
for kv in kvs:
    print(kv)

#------------------
for kv in kvs:
    print(kv[0],"--->",kv[1])

#----------------
for k,v in d1.items():
    print(k,"---->",v)