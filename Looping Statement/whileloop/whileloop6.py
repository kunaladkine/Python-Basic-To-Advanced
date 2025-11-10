#program for generating Mul Table for Given N where is +ve.
#whileloop6.py

n=int(input("enter Any Integer Value for generating Mul Table:"))
if(n<=0):
    print("\t{} Invalid".format(n))
else:
    print("_"*50)
    print("\tMul Table for {}".format(n))
    print("_"*50)
    i=1
    while(i<11):
        print("\t{} x {} = {}".format(n,i,n*i))
        i+=1
    else:
        print("_"*50)