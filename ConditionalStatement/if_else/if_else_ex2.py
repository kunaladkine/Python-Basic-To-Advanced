#program for reading a numerical value decide whetehr it is +ve or -ve or zero by using if else statement.
value=float(input("Enter Any Value:"))
if(value>0):
    print("{} is +Ve Value.".format(value))
else:
    if(value<0):
        print("{} is -ve Value.".format(value))
    else:
        print("{} is Zero.".format(value))
print("Program Executed Completed.")