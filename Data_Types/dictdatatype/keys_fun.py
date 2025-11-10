#syntax : varname=DictObj.keys()
#this function is used for obtaining values of key and place the values of key in LHS varname and whose type is <class dict_key>

statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps,type(statescaps))

states=statescaps.keys()
print(states)

#---------------
for k in states:
    print(k)

#----------------------

for k in statescaps.keys():
    print(k)

#-----------------
for de in enumerate(statescaps):
    print(de)

#----------------------
for de in enumerate(statescaps):
    print(de,"----->",statescaps[de[1]])

#-------------
for de in enumerate(statescaps):
    print(de,"---->",statescaps.get(de[1]))