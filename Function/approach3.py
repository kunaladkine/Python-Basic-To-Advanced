#define function for addition of two numbers
#approach 3

def addop(k,v):
    r=k+v
    print("Sum({},{})={}".format(k,v,r))

#main program
k=float(input("Enter First Value:"))
v=float(input("Enter Second Value:"))
addop(k,v)  #function call