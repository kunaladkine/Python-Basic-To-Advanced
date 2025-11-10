#program for generating N to 1 Numbers where N is +ve number
n=int(input("Enter How Many numbers u want to generate:"))
if(n<=0):
    print("\t{} is Invalid".format(n))
else:
    print("_"*50)
    print("Numbers form {} to 1".format(n))
    print("_"*50)
    i=1
    while(i>=1):
        print("\t{}".format(i))
        i=i-1
    else:
        print("_"*50)