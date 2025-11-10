#program for accepting three numerical values and find biggest and check for equality

a=float(input("Enter Value a : "))
b=float(input("Enter Value b : "))
c=float(input("Enter Value c : "))

res=a if (a>b) and (a>c) else b if (b>a) and (b>c) else c if (c>a) and (c>b) else "Both Value are Equal"
print("Max ( {},{},{})={}".format(a,b,c,res))