#program for demonstrating with decorator (function in functions-nested functions)

def square(x):
    def calculate():        #inner function
        n=x()
        res=n**2        #local variable
        return n,res
    return calculate

def getvalue():
    return float(input("Enter Any Numerical Value: "))

#main program
res=square(getvalue)()
print("Square({})={}".format(res[0],res[1]))