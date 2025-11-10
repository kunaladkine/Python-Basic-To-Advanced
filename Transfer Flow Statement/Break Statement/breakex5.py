#program for accepting a numerical integer value and decide wheteher it is prime or not

n=int(input("Enter Any Integer Value :"))
if(n<1):
    print("\t{} Invalid Input".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOT PRIME"
            break
    print("\t{} is {}".format(n,res))