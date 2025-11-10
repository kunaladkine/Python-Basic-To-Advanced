#program for showing the need of closures

def operation(a):
    b=10
    def processval(c):
        res=a+b+c
        print("a={} b={} c={} sum={}".format(a,b,c,res))
    return processval

#main program
pv=operation(10)
pv(100)     #inner function call
pv(200)     #inner function call
pv(300)