#program for generating all even numbers in reverse order withinng the range .
'''
n=int(input("Enter how many even number u want to generate :"))
if(n<=0):
    print("\t\t{} invalid number .".format(n))
else:
    if(n%2!=0):
        n=n-1
    print("_"*50)
    for i in range(n,0,-2):
        print("\t{}".format(i))
    else:
        print("_"*50)

'''

n=int(input("Enter Any Number : "))
if(n<=0):
    print("Invalid Input")
else:
    if(n%2!=0):
        n=n-1
    else:
        for i in range(n,0,-2):
            print(i)
        else:
            print('program executed completed...!')