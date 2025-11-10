from ATMExcept import DepositError,WithDrawError,InsuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice :"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDont Try To Depost -ve/Zero Value")
                    print("\tDont Enter Alnum, Strs and Symbols as Deposit Amount")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDon't Try To Withdraw -Ve/Zero Value")
                except InsuffFundError:
                    print("\tUr Account Does not contain sufffund")
                except ValueError:
                    print("\tDon't Enter Alnums, Strs and Symbols as Withdraw Amount")
            case 3:
                balenq()
            case 4:
                print("thx for using this project")
                break
            case _:
                print("\tUr Selection of Operations is Wrong - try again")
    except ValueError:
        print("\tDon't Enter Alnums, Strs and symbols for Choice:")
