import pickle
def updateemploye():
    eno=int(input("Enter Emp Number To Update Salary aand Comany Name:"))
    #Get All the records from file
    records=[]
    with open("empproj.pick","rb")as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #Tracing for Finding the record
    found=False
    for index in range(0,len(records)):
        if(records[index][0]==eno):
            recindex=index
            found=True
            break
    if(found):
        #update salary and comp name
        newsal=float(input("Enter New Salary:"))
        compname=input("Enter New Comp Name:")
        records[recindex][2]=newsal
        records[recindex][3]=compname
        #Re-Write Update Records to Fle
        with open ("emproj.pick","wb")as fp:
            for record in records:
                pickle.dump((record,fp))
        print("\tEmploye Record Updated --verify")
    else:
        print("\tEmployee Number {} Does Not Exist".format(eno))