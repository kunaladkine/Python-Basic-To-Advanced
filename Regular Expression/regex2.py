#program for searching python word in given data
import re
gd="Python is an oop lang"
sp="python"
result=re.search(gd,sp)
if (result!=None):
    print("_"*50)
    print("{} word find successful".format(result))
else:
    print("_"*50)
    print("{} word not find successful".format(sp))
    print("_"*50)