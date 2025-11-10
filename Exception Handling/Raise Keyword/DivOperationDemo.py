from DivExcept import DenError
from DivOperation import division
try:
    a=int(input("Enter  First Value:"))
    b=int(input("Enter Second Value:"))
    res=division(a,b)       #function call
except DenError:
    print("\tDont Ente Zero for Den")
except ValueError:
    print("\tDont Enter Alnum,str and symbols")
else:
    print("Div({},{})={}".format(a,b,res))

#phase 3 : handling the exception along with result
