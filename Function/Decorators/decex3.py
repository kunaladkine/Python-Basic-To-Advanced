#program for demonstrating with decorator (function in functions-nested functions)

def square(gv):
    def calculate():        #inner function
        n=gv()
        res=n**2        #local variable
        return n,res
    return calculate
@square
def getvalue():
    return float(input("Enter Any Numerical Value: "))

#main program
k,v=getvalue()
print("Square({})={}".format(k,v))
