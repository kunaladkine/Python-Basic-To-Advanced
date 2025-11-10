#Multiline Exeception Handling 

try:
    print("Program Execution Started")
    s1=input("\tEnter First Value:")
    s2=input("\tEnter Second Value:")
    #convert str to int type
    a=int(s1)
    b=int(s2)
    c=a/b
except (ZeroDivisionError,ValueError):
    print("\tDon't Enter Zero For Den")
    print("\tDon't Enter Alnum,str,and symbols")
else:
    print("_"*50)
    print("\tValue of a={}".format(a))
    print("\tValue of b={}".format(b))
    print("Div={}".format(c))
finally:
    print("Program Executed Completed")