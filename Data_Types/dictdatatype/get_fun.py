#Syntaxx : varname=dictobj.get(Key)
#this function is used for obtaining the value of value by passing the value of key.

#syntax : DictObj[key]

d1={10:1.2,20:2.2,30:3.3,40:4.4}
print(d1,type(d1),id(d1))

val=d1.get(10)
print(val)

print(d1.get(20))
print(d1.get(30))

print(d1.get(200))      #we get none or space , not present key
#------------------


statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)

print(statescaps.get("TS"))
print(statescaps.get("KAR"))
print({}.get(10))       #none

