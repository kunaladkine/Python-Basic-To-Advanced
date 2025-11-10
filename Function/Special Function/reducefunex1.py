#program for accepting list of numerical values and find their sum by using reduce()
#reducefunex1.py

import functools
def sumop(k,v):
    return k+v

#main program
# print("Enter List of Numerical values separated by comma:")
lst=[float(val) for val in input("Enter Numerical Val:").split()]
sumval=functools.reduce(sumop,lst)
print("Sum({})={}".format(lst,sumval))