#program for cal area of circle

def getradius():
    return float(input("Enter Radius:"))
def calarea(r):
    ac=3.14*r**2
    return ac
def dispresult():
    r=getradius()       #function call
    if(r<=0):
        print("\t{} is Invalid input".format(r))
    else:
        ac=calarea(r)       #function call
        print("Radius of Circle={}".format(r))
        print("Area of Circle={}".format(ac))

#main program
dispresult()        #function call