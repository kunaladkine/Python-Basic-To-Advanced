#Syntax : varname=DictObj.values()
#this function is used for obtaining values of value and places the values of values in LHS varname and whose type is <class 'dict_values'>
from traceback import print_tb

statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps,type(statescaps))

caps=statescaps.values()
print(caps,type(caps))
#------------
print("-----------")
for v in caps:
    print(v)

print("---------------------")
#------------
for v in statescaps.values():
    print(v)

print("----------------")
#------------------

