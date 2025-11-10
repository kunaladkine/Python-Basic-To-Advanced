#program for Generaing 1 to N Number where n is +ve
n=int(input("Enter How Many Positive No Want :"))
if(n<=0):
    print("\t{} Invalid Input")
else:
    print("_"*50)
    print("\tPositive No : {}".format(n))
    print("_"*50)
    for i in range(1,n+1):
        print(i)
    else:
        print("Program Executed Completed.")

'''
n=int(input("Enter How Many No U Want :"))
if(n<=0):
    print("\t\t{} Invalid Input - try again")
else:
    for i in range(1,n+1):
        print(i)
    else:
        print("Program Executed Completed...!")


n=int(input("Enter Any Number:"))
if(n<=0):
    print("{} invalid input.".format(n))
else:
    for i in range(0,n+1):
        print(i)
    else:
        print("Program Executed Completed...!")'''