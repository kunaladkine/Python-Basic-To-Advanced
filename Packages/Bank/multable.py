def table(n): # Function Definition
    if(n<=0):
        print("\t{} Is invalid input".format(n))
    else:
        print("-"*50)
        print("\tMul Table for:{}".format(n))
        print("-" * 50)
        for i in range(1,11):
            print("\t{} x {} = {}".format(n,i,n*i))
        print("-" * 50)