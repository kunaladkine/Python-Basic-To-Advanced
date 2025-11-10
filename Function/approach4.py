#define functionn for addition of two numbers
#appracch4.py

def addop():
    #taking input
    k=float(input("Enter First Value:"))
    v=float(input("Enter Second Value:"))
    #Do the process
    r=k+v
    return k,v,r    #by using return kwd,we can return one or more number of values

#main program

k,v,r=addop()   #function call with multi line assignment
print("Sum({},{})={}".format(k,v,r))
print("_"*50)
res=addop()     #function call with single line assignment
#here res is an object of <class, tuple>
print("Sum({},{})={}".format(res[0],res[1],res[2]))
