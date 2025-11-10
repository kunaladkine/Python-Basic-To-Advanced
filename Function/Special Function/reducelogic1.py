import functools
def sumop(k,v):
    return k+v

#main program
lst=[10,20,30,40,50]
res=functools.reduce(sumop,lst)
print("The Sum is ({})={}".format(lst,res))