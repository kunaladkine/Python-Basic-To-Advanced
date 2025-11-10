#write a program to find multiple of 5 and 3 and if both multiple show them.
value=int(input("Enter Any Value:"))
if(value<0):
    print("Invalid Input.")
else:
    if(value%3==0)and(value%5==0):
        print("{} is Multiple of Both.".format(value))
    else:
        if(value%3==0):
            print("{} is Multiple of 3".format(value))
        else:
            print("{} is Multiple of 5".format(value))
print("Program Executed Completed.")