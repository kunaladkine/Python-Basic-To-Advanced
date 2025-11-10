from MulExcept import ZeroError,NegNumberError
from MulTable import table
while(True):
    try:
        num=int(input("enter Any number:"))
        table(num)
    except NegNumberError:
        print("\tDont Enter -ve number")
    except ZeroError:
        print("\tDont enter zero for mul table")
    except ValueError:
        print("\tDont Enter Alnum,Str, and Symbols")
    except:
        print("\t Opps something is wrong")
    else:
        break