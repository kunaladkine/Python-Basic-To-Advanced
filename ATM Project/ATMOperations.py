from ATMExcept import DepositError,WithDrawError,InsuffFundError
bal=500.00      #here bal is called Global Variables
def deposit():
    damt=float(input("Enter Ur Depost Amount:"))        #chance of raising ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUr Account xxxxx123 Credited with INR:{}".format(damt))
        print("\tUr Account xxxxx123 Bal after Deposit:{}".format(bal))

def withdraw():
    global bal
    wamt=float(input("Enteer Ur Withdraw Amount:")) #chance of raissing ValueError
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InsuffFundError
    else:
        bal=bal-wamt
        print("\tUr Account xxxxx123 Debited with INR:{}".format(bal))

def balenq():
    print("\tUr Account xxxxx123 Bal:{}".format(bal))