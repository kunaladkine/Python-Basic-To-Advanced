#DivOperation.py

from DivExcept import DenError
def division(a,b):
    if(b==0):
        raise DenError
    else:
        return (a/b)

#Phase-2 : Development of Business Logic and Hitting the Exception