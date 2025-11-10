def multable(n):
    if(n<=0):
        print("\t{}Is Invalid Input".format(n))
    else:
        print("_"*50)
        print("\tMul Table for :{}".format(n))
        print("_"*50)
        for i in range(1,11):
            print("\t{}x{}={}".format(n,i,n*i))
        print("_"*50)
