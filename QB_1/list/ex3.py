#python program to find largest number in a list

import functools
lst=[float(val) for val in input("Enter List Values:").split()]
maxval=functools.reduce(lambda k,v:k if k>v else v,lst)
print("The Largest Value is :",maxval)