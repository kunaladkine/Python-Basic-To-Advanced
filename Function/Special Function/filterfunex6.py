def isprime(n):
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
    return res

#main program
print("Enter listof integear values separated by space for getting primes")
lst=[int(val) for val in input().split() if int(val)>0]
print("List of Values")
print(lst)
primelist=list(filter(isprime,lst))
print("List of Primes")
print(primelist)