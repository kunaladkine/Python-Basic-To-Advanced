#program for accepting a numerical integer value and decide wheteher it is prime or not

n=int(input("Enter Any Integer Value :"))
if(n<1):
    print("\t{} Invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
    res="PRIME" if res else "NOT PRIME"
    print("\t{} is {}".format(n,res))