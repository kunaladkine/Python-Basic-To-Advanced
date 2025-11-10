#program for demonstrating with decorator


def cube(procv):
    def calculate():
        n,sqv,sqrtv=procv()
        cbv=n**3
        return n,sqv,sqrtv,cbv
    return calculate

def squareroot(calc):
    def processval():
        n,sqv=calc()
        sqrtv=n**0.5
        return n,sqv,sqrtv
    return processval

def square(gv):
    def calculate():
        n=gv()
        res=n**2
        return n,res
    return calculate

@cube
@squareroot
@square
def getval():
    return float(input("Enter Any Numerical Value:"))

#main program
res=getval()
print("Square({})={}".format(res[0],res[1]))
print("SquareRoot({})={}".format(res[0],res[2]))
print("Cube({})={}".format(res[0],res[3]))