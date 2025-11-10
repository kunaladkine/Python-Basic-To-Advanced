#program for cal product of n natural numbers
n=int(input("Enter how many natural nums product u want:"))
if(n<=0):
    print("Invalid Input")
else:
    prod=1      #multiplicative identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        prod=prod*i
    else:
        print("product=",prod)