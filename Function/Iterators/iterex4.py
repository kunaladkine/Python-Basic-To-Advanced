from Function.Iterators.iterex2 import itrobj

x={1:"Python",2:"C",3:"C++",4:"Java"}
print("_"*50)
print("Content of Iterable Object={}, Type:{}".format(x,type(x)))
itrobj=iter(x)
print("Content of Iterator={} Type:{}".format(itrobj,type(itrobj)))
print("_"*50)

#code for Getting the Values for Iterator Object
while(True):
    try:
        ks=next(itrobj)
        print("\t{}-->{}".format(ks,x[ks]))
    except StopIteration:
        print("_"*50)
        break