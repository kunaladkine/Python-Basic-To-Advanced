#Programm for Generating Listof Primes for n Random Dynamic Numbers where N is +Ve

ran=int(input("Enter the Number of Values, in which list the prime:"))
if(ran<=0):
    print("\t{} is Invalid Input".format(ran))
else:
    lst=[]
    for i in range(1,ran+1):
        value=int(input("Enter {} value:".format(i)))
        lst.append(value)
    else:
        print("list of Random Values")
        print(lst)
        print("List of Primes Withing : {}".format(ran))
        for num in lst:
            if(num<=1):
                continue
            res=True
            for i in range(2,num):
                if(num%i==0):
                    res=False
                    break
            if(res):
                print(num)