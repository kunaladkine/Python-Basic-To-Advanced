#program for generating list of prime for n within the range where N is +Ve
ran=int(input("Enter teh range, in which lsit the primes:"))
if(ran<=0):
    print("\t{} is Invalid INput".format(ran))
else:
    print("List of Prime Withing :{}".format(ran))
    nop=0
    for num in range(1,ran+1):
        if(num<=1):
            continue
        res=True
        for i in range(2,num):
            if(num%i==0):
                res=False
                break
        if(res):
            print("\t{}".format(num))
            nop=nop+1
    else:
            print("Numbers of Primes Withing {}={}".format(ran,nop))