#program to call div of Two Numbers
try:
    print("Program Execution Started")
    s1=input("\tEnter First Value:")
    s2=input("\tEnter Second Value:")
#convert str data into int type
    a=int(s1)       #Exception generated stmt---ValueError
    b=int(s2)

#cal Div
    c=a/b      #Exception generated stmt-----ZeroDivisionError
except ZeroDivisionError:
    print("\tDon't Enter Zero For Den")
except ValueError:
    print("\tDon't Enter Alnum,strs,and symbols")
else:
    print("\tValue of a={}".format(a))
    print("\tValue of b={}".format(b))
    print("\tDiv={}".format(c))
finally:
    print("Program Execution Completed")