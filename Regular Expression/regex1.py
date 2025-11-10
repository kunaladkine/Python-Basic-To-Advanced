import re
gd="Python is an oop language"
sp="Python"
result=re.findall(sp,gd)
if (len(result)!=0):
    print("\t {} Word is find successful".format(result))
    print("\t {} occurance of {}".format(sp,len(result)))
    print("_"*50)
else:
    print("\tWord is not find successful")