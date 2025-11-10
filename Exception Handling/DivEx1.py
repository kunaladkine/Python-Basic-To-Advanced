#program to call div of Two Numbers
print("Program Execution Started")
s1=input("\tEnter First Value:")
s2=input("\tEnter Second Value:")
#convert str data into int type
a=int(s1)       #Exception generated stmt---ValueError
b=int(s2)
print("\tValue of a={}".format(a))
print("\tValue of b={}".format(b))
#cal Div
c=a/b      #Exception generated stmt-----ZeroDivisionError
print("\tDiv={}".format(c))
print("Program Execution Completed")