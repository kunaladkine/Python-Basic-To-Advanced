#program for accepting two numerical values and find biggest among them and check for equality

findbig=lambda k,v:k if k>v else v if v>k else "both Value are Equal"

#main program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
res=findbig(a,b)    #normal function call
print("Max({},{})={}".format(a,b,res))
