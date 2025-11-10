#program for demonstrating the need of globals()

def operation():
    x=globals()
    print("_"*50)
    print("Number of Global Variables=",len(x))
    print("Invisible and Programmer-Definned global Variables")
    print("_"*50)
    for gvn,gvv in x.items():
        print("\t{}-->{}".format(gvn,gvv))
    print("_"*50)
    print("Programmer-Defined global Variables-Way-1")
    print("_"*50)
    print("\tGlobal Var a=",x.get('a'))
    print("\tGlobal Var b=",x.get('b'))
    print("_"*50)
    print("Programmer-Defined global Variable-Way-2")
    print("_"*50)
    print("\tGlobal Var a=",x['a'])
    print("\tGlobal Var b=",x['b'])
    print("_"*50)
    print("Programmer-Defined global Variables-Way-3")
    print("_"*50)
    print("\tGlobal Var a=",globals()['a'])
    print("\tGlobal Var b=",globals()['b'])
    print("_"*50)
    print("Programmer-Defined global Variables-way-4")
    print("_"*50)
    print("\tGlobal Var a=",globals().get('a'))
    print("\tGlobal Var b=",globals().get('b'))
    print("_"*50)

#main program
a=10
b=20    #here a and b are called global variables
operation()     #function call
