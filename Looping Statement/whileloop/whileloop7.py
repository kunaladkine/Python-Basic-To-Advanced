#write a python program which will generate all odd numbers  within n
n=int(input("Enter Any Integer Number :"))
if(n<=0):
    print("\t{} Invalid".format(n))
else:
    print("_"*50)
    print("\t odd Number Is {} ".format(n))
    print("_"*50)
    i=20
    while(i>=n):
        print("\t{}".format(i))
        i-=2
    else:
        print("Program Executed completed")