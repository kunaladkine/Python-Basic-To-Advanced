#Exception as alias Name

try:
    print("Program Execution Started")
    s1=input("\tEnter First Value:")
    s2=input("\tEnter Second Value:")
    #convert str into int type
    a=int(s1)
    b=int(s2)
    #div
    c=a/b
except ZeroDivisionError as z:
    print("\t{}".format(z))
except ValueError as v:
    print("\t{}".format(v))
else:
    print("_"*50)
    print("\tValue of a={}".format(a))
    print("\tValue of b={}".format(b))
    print("\tDiv={}".format(c))
finally:
    print("Program Execution Completed")