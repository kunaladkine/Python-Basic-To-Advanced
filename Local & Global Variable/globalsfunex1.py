#program for demonstrating the need of globals()
#in this program, we have unique global and Local Variables Names

a=10
b=20
c=30
d=40        #here a,b,c,d are called global variables

def operation():
    x=100
    y=200
    z=300
    k=400       #here x,y,z,k are local variables
    res=a+b+c+d+x+y+z+k
    print("Result=",res)

#main program
operation() #function call