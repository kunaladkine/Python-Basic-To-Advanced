import pickle
def searchemploye():
    eno=int(input("Enter Employee Number to Search:"))
    #get all the records from file
    records=[]
    with open("empproj.pick","rb")as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #To Display emp details
    found=False
    for record in records:
        if(record[0]==eno):
            found=True
            break
    print("_"*50)
    if(found):
        print("\tEmployee Working In Organization--Valid Employee")
    else:
        print("\tEmployee is Not Working in Organization Invalid Employee".format(eno))
    print("_"*50)