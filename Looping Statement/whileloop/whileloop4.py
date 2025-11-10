#program for generating all even numbers withing in N, where N is +ve
#whileloopex4.py

n=int(input("Enter How Many Even Numbers u want to Generate within the range:"))
if(n<=0):
    print("\t{} invalid".format(n))
else:
    print("_"*50)
    print("\tEven Numbers withing {}".format(n))
    print("_"*50)
    i=2
    while(i<=n):
        print("\t{}".format(i))
        i=i+2
    else:
        print("_"*50)