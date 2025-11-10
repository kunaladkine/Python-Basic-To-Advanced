
#program for demosnstrating with decorator (Functioin in Function--Nested Functions)

def square(x):              #outer function
    def calculate():        #inner function
        n=x()
        res=n**2
        return n,res
    return calculate
def getval():
    return float(input("Enter Anu Numerical Value:"))

#main program
calc=square(getval)
res=calc()
print("Square({})={}".format(res[0],res[1]))

