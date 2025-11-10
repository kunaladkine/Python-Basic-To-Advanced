#level2ex
#program for call sum of n natural numbers.
n=int(input("Enter How many Natural Nums Sum Want:"))
if(n<=0):
    print("Invalid Input.")
else:
    s=0 #ADditive identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s+i
    else:
        print("_"*50)
        print("sum={}".format(s))
        print("*"*50)