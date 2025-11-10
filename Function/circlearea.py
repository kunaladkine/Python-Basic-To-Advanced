#program for cal area of circle

def getradius():
    return float(input("Enter Radius:"))

def calarea(r):
    ac=3.14*r**2
    return ac

def dispresult(r,ac):
    print("Radius of Circle={}".format(r))
    print("Area of Circle={}".format(ac))\

#main program
r=getradius()       #function call
ac=calarea(r)       #function call
dispresult(r,ac)        #function call