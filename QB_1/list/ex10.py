# Python program to find sum of elements in list
import functools
lst=[10,20,45,65]
svale=functools.reduce(lambda k,v:k+v,lst)
print("The Sum of List Value is :",svale)

s=0
lst=[10,20,45,65]
for val in lst:
    s=s+val
    print(s)