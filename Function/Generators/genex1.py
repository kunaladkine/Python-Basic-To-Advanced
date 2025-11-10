#program for show the need of generator

def kvrrange(Val):
    i=1
    while(i<=Val):
        yield i
        i=i+1


#main program
r=kvrrange(6)
print("Type of r=",type(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
