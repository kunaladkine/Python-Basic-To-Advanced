from Function.Iterators.iterex1 import itrobjt

x=(10,"RS",45.67,True)
print("_"*50)
print("Content of Iterable Oject={}, Type:{}".format(x,type(x)))
print("_"*50)
itrobj=iter(x)
print("Content of Iterator={} Type:{}".format(itrobj,type(itrobj)))
print("_"*50)

#code for getting the values for Iterator Object
while(True):
    try:
        print(next(itrobj))
    except StopIteration:
        print("_"*50)
        break