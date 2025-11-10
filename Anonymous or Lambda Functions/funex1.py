#program for adding two values by using annoymous functions

sumop=lambda a,b: a+b   #anonymous function def

#main program
a=float(input("Enter First Value:"))
b=float(input("Enter Second Value:"))
res=sumop(a,b)  #normal function call
print("Sum({},{})={}".format(a,b,res))