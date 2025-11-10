#define function for addition of two numbers

def addop():
    #Taking the input in function body
    a=float(input("Enter First Value:"))
    b=float(input("Enter Second Value:"))
    #processing the input
    c=a+b
    #display the result --here a ,b,c are local varable
    print("Sum({},{})={}".format(a,b,c))

#main program
addop()