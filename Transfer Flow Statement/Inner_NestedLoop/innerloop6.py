#program for generating mul tables for n random dynamic numberss where n is +Ve

n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("\t {} In Invalid Number".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        value=int(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("List of Random Values")
        print(lst)
        for num in lst:
            if(num<=0):pass
            else:
                print("Mul Table for:{}".format(num))
                print("_"*50)
                for i in range(1,11):
                    print("\t{} x {} = {}".format(num,i,num*i))
                print("_"*50)