#program for generating 1 to N Numbers where N is +ve Number
#whileloop.py

n=int(input("Enter How Many Numbers u want To Generatre :"))
if(n<=0):
    print("\t{} is Invalid".format(n))
else:
    print("_"*50)
    print("Numbers Withing :{}".format(n))
    print("_"*50)
    i=1 #inititzation part
    while(i<=n): #condition part
        print("\t{}".format(i))
        i=i+1       #updation part
    else:
        print("_"*50)
    print("Program Execution Completed.")