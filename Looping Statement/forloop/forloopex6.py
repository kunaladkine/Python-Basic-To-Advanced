#program for generating mul table for givne n is +ve number
n=int(input("enter any integer value:"))
if(n<=0):
    print("Invalid Input.")
else:
    for i in range(1,11):
        print("\t\t{}*{}={}".format(n,i,n*i))
    else:
        print("_"*50)