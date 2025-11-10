#program for cal factorial of number n!=1*2*3*4*5
n=int(input("Enter a Number fr cal Factorial:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    fact=1      #multiplicative identity
    for i in range(1,n+1):
        fact=fact*i
    else:
        print("Factorial({}!)={}".format(n,fact))