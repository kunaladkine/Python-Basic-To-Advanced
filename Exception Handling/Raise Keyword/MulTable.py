from MulExcept import ZeroError,NegNumberError
def table(n):
    num=int(n)
    if(num==0):
        raise ZeroError
    elif(num<0):
        raise NegNumberError
    else:
        print("_"*50)
        print("\t\tMul Table for :{}".format(num))
        print("_"*50)
        for i in range(1,11):
            print("\t\t{} x {}={}".format(n,i,num*i))
        print("_"*50)
