#program for generating all even Numbers Within in N, where N is +ve
n=int(input("Enter how Many Even Numbers u want to Generate with the Range:"))
if(n<=0):
    print("\t{} invalid ".format(n))
else:
    print("_"*50)
    print("\t Even Numbers Withing {}".format(n))
    print("_"*50)
    i=1
    while(i<=n):
        if(i%2==0):
            print("\t{}".format(i))
        i=i+1
    else:
        print("_"*50)