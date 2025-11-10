#write a python program which will accept any numerical value and decide it is positive or negative value.

value=float(input("Enter Any Value:"))
if (value>=0):
    print("{} is positive".format(value))
if (value<=0):
    print("{} is Negative".format(value))
print("Program Executed Successfully....!")