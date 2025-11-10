#python program to find smallest number in a list

import functools
print("Enter list of Numerical values spearated by comma:")
lst=[float(val) for val in input().split(",")]
minval=functools.reduce(lambda x,y:x if x<y else y,lst)
print("Min({})={}".format(lst,minval))