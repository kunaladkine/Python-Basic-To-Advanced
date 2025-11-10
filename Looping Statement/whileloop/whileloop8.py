##write a python program which will generate all odd numbers  within n in reverse .
n=int(input("Enter Any Integer Number :"))
if(n<=0):
    print("\t{} Invalid".format(n))
else:
    print("_"*50)
    print("\t odd Number Is {} ".format(n))
    print("_"*50)
    i=n-1
    while(i>=0):
        if(i%2!=0):
            print("\t{}".format(i))
        i=i-1
    else:
        print("Program Executed completed")

