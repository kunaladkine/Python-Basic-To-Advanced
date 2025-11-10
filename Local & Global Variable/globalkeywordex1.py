#program for demonstrating global keyword

def increment():
    global a
    a=a+1
def modify1():
    global a
    a=a*2

#main program
a=10        #here a is call global Variable
print("Main Program: Value of A Before increment():{}".format(a))

increment() #function call
print("Main Program : Value of a after increment():{}".format(a))

modify1()   #function call
print("Main Program : Value of A After Modify () :{}".format(a))