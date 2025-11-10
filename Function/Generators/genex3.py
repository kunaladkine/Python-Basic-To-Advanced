#program for show the need of generator

def kvrrange(Begin,End):
    while(Begin<=End):
        yield Begin
        Begin=Begin+1

#main program
r=kvrrange(10,20)
print("Type of r=",type(r))
for val in r:
    print(val)
print("_"*50)
r=kvrrange(100,105)
print("Type of r=",type(r))
for val in r:
    print(val)