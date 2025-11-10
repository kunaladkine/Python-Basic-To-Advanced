#program for generating 1 to N mul Tables where N is +ve

n=int(input("Enter How Many Mul Table u want:"))
if(n<=0):
    print("\t{} Is Invalid Input".format(n))
else:
    for num in range(1,n+1):
        print("_"*50)
        print("\tMul Table for:{}".format(num))
        print("_"*50)
        for i in range(1,11):
            print("\t{} x {}={}".format(num,i,num*i))
        else:
            print("_"*50)