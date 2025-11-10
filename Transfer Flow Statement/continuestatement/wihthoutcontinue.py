n=int(input("Enter How Many Values u Have :"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        value=float(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("List of Values")
        print(lst)
        ps,ns,pslist,nslst=0,0,list(),list()
        for val in lst:
            if(val>0):
                ps=ps+val
                pslist.append(val)
            else:
                ns=ns+val
                nslst.append(val)
        else:
            print("\tList of +Ve Values")
            print("\t{}".format(pslist))
            print("+Ve vals sum=",ps)
            print("\tList of - Ve Values")
            print("\t{}".format(nslst))
            print("-Ve Vals Sum=",ns)