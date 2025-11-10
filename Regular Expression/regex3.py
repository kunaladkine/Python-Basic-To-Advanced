import re
gd="python is an oop lang"
sp="python"
result=re.finditer(gd,sp)
for mat in result:
    print("Start Index {} End Index {}".format(mat.start(),mat.end()))
    print("_"*50)