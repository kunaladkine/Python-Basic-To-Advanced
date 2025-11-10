#program for show the need of generator

def kvrrange(Begin,End,Step):
    while(Begin<=End):
        yield Begin
        Begin=Begin+1

#main program
r=kvrrange(10,20,2)
print("Type of r=",type(r))
for val in r:
    print(val)
print("_"*50)
r=kvrrange(100,151,10)
print("Type of r=",type(r))
for val in r:
    print(val)
print("_"*50)