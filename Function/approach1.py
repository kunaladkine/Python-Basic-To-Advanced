#define function for additon of two numbers .
#appraoch 1

def addop(a,b):     #here a and b are called formar parameters
    c=a+b   #here c is called local variable processing the input
    return c
#main program
k=float(input("Enter First Value:"))
v=float(input("Enter Second Value:"))
r=addop(k,v)    #function call -- taking input to the function call

print("Sum({},())={}".format(k,v,r))
print("_"*50)
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
c=addop(a,b)        #function call
print("sum({},{})={}".format(a,b,c))
