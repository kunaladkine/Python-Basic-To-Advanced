#program for accepting list of numerical values and find their sum by using reduce()
#reducefunex2.py

import functools
lst=[float(val) for val in input("Enter Values:").split(",")]
sumval=functools.reduce(lambda k,v:k+v,lst)
print("({})={}".format(lst,sumval))