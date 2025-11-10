#program for demonstrating global keyword

def increment():
    global a,b
    a=a+1
    b=b+1

def modify1():
    global a,b
    a=a*2
    b=b*2

#main program
a,b=10,20       #here a and b are called global variables
print("Main Program: before increment() a:{} b:{}".format(a,b))

increment() #function call
print("Main Program : after increment() a:{} b:{}".format(a,b))

modify1()       #function call
print("Main Program : after modify1() a:{} b:{}".format(a,b))