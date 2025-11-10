#program for accepting list of numerical values and find max and min by siing reduce()
#redcuefunex3.py

import functools
print("Enter list of Numerical values spearated by comma:")
lst=[float(val) for val in input().split(",")]
maxval=functools.reduce(lambda k,v:k if k>v else v,lst)
minval=functools.reduce(lambda x,y:x if x<y else y,lst)
print("Max({})={}".format(lst,maxval))
print("Min({})={}".format(lst,minval))