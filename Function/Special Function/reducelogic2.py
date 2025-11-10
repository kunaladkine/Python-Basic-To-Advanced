import functools
lst=[10,20,30,40]
print("Given List is:",lst)
res=functools.reduce(lambda k,v:k+v,lst)
print("The Total Sum of lst ={}".format(res))