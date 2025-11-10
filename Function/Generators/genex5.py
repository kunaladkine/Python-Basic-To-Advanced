#program for show the need of generator

def kvrrange(Begin,End=0,Step=1):
    if(Begin>End):
        End=Begin
        Begin=1
    while(Begin<=End):
        yield Begin
        Begin=Begin+Step

#main program
r1=kvrrange(6)
for val in r1:
    print(val)
print("_"*50)
r2=kvrrange(10,15)
for val in r2:
    print(val)
print("_"*50)
r3=kvrrange(100,151,10)
for val in r3:
    print(val)
print("_"*50)