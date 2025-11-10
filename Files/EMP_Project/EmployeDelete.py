import pickle
def deleteemploye():
    eno=int(input("Enter Emp Number To Delete:"))
    #get all the records from file
    records=[]
    with open("empproj.pick","rb")as fp:
        while(True):
            try:
              record=pickle.load(fp);
              records.append(record)
            except EOFError:
                break
    #Tracing for finding the record
    found=False
    for index in range(0,len(records)):
        if(records[index][0]==eno):
            recindex=index
            found=True
            break
            #decide the  record found or not
    if(found):
        records.remove(records[recindex])
        with open("empproj.pick","wb")as fp:
            for record in records:
                pickle.dump(record,fp)
        print("\tEmployee Record Deleted ---verify")
    else:
        print("\tEmployee Number {} Does Not Exist".format(eno))
