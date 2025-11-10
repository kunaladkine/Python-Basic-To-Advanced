#program for demonstrating the need of globals()
#in this program, we have unique global and Local Variables Names

a=10
b=20
c=30
d=40        #here a,b,c,d are called global variables

def operation():
    a=100
    b=200
    c=300
    d=400       #here a,b,c,d are local variables
    res=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
    print("Result=",res)

#main program
operation() #function call