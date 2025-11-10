#program for show the need of generator

def kvrrange(Val):
    i=1
    while(i<=Val):
        yield i
        i=i+1

#main program
r=kvrrange(10)
print("Type of r=",type(r))
for val in r:
    print(val)