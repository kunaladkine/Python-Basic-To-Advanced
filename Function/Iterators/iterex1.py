x=[10,"RS",45.67,True]
print("_"*50)
print("Content of Iterable Object={},Type:{}".format(x,type(x)))
print("_"*50)
itrobjt=iter(x)
print("Content of Iterator={} Type:{}".format(itrobjt,type(itrobjt)))
print("_"*50)
print(next(itrobjt))
for val in itrobjt:
    print(val)
