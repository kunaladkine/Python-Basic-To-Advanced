#program for generating all odd numbers in reverse order within the range.
'''
n=int(input("Enter How Many Odd Number U want to generate : "))
if(n<=0):
    print("{} invalid input".format(n))
else:
    if(n%2==0):
        n=n-1
        for i in range(n,0,-2):
            print("\t{}".format(i))
        else:
            print("Program executed completed .")
'''


n=int(input("Enter value :  "))
if(n<=0):
    print("invaid no")
else:
    if(n%2==0):
        n=n-1
    print("_"*50)
    for i in range(n,0,-2):
        print("\t\t{}".format(i))
    else:
        print("_"*50)
