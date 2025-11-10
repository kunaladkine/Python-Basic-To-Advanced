#program for accepting a Digit and Display Its Name

d=int(input("Enter Any Digit:"))
if(d==0):
    print("{} is Zero.".format(d))
elif (d==1):
    print("{} is One".format(d))
elif(d==2):
    print("{} is Two".format(d))
elif(d==3):
    print("{} is Three".format(d))
elif(d==4):
    print("{} is Four".format(d))
elif(d==5):
    print("{} is Five".format(d))
elif(d==6):
    print("{} is Six".format(d))
elif(d==7):
    print("{} is Seven".format(d))
elif(d==8):
    print("{} is Eight".format(d))
elif(d==9):
    print("{} is Nine".format(d))
elif(d>9):
    print("{} is Positive Number.".format(d))
elif(d<0) and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("\t{} is -VE NUMBER".format(d))
elif(d<0) and d in range(-1,-10,-1):
    print("\t{} is -VE DIGIT".format(d))
