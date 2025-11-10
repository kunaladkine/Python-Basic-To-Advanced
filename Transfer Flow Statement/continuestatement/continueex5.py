n=int(input("Enter How many values u have:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        value=float(input("Enter {} value:".format(i)))
        lst.append(value)
    else:
        print("List of Values")
        print(lst)
        ps=0
        pslist=[]
        for val in lst:
            if(val<=0):
                continue
            ps=ps+val
            pslist.append(val)
        else:
            print("\tList of +ve values")
            print("\t",pslist)
            print("\tSum of +ve Values=",ps)
            ns=0
            nglist=list()
            for val in lst:
                if(val>0):
                    continue
                ns=ns+val
                nglist.append(val)
            else:
                print("\tList of -ve values.")
                print("\t",nglist)
                print("\tSum of -ve Values=",ns)