from Function.Iterators.iterex4 import itrobj

x="PYTHON"
print("_"*50)
print("Content of Iterable Object={},Type:{}".format(x,type(x)))
print("_"*50)
itrobj=iter(x)
print("Content of Iterator={} Type:{}".format(itrobj,type(itrobj)))
print("_"*50)

#code for Getting the Valuess for Iterator Object
while(True):
    try:
        print(next(itrobj))
    except StopIteration:
        print("_"*50)
        break