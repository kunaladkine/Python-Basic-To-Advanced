#NameValidationDemo.py
from NameExcept import ZeroLengthError, SpaceError, InvalidNameError
from NameValidation import validation
while(True):
    try:
        name=input("Enter Ur Name:")
        vname=validation(name) # Function call--gives result or exception
    except ZeroLengthError:
        print("\tU Must Enter Ur Name--try again")
    except SpaceError:
        print("\tDon't Enter Space for Ur Name--try again")
    except InvalidNameError:
        print("\t'{} is Invalid Name-try again".format(name))
    else:
        print("UR Name=",vname)
        break