import pickle
def viewemploye():
    eno=int(input("Enter Employe Number to view Details:"))
    #get all the records from file
    records=[]
    with open("empproj.pick","rb")as fp:
        while(True):
            try:
                record=pickle.load(fp)
                records.append(record)
            except EOFError:
                break
    #to dispaly emp details
    found=False
    for record in records:
        if(record[0]==eno):
            rec=record
            found=True
            break
    print("_"*50)
    if(found):
        print("\tEmployee Number: {}".format(rec[0]))
        print("\tEmploye Name: {}".format(rec[1]))
        print("\tEMploye Salary: {}".format(rec[2]))
        print("\tEmploye Comp Name: {}".format(rec[3]))
    else:
        print("\tEmploye Number {} Does not Exist".format(eno))
    print("_"*50)

def viewallemployes():
    with open("empproj.pick","rb")as fp:
        print("_"*50)
        print("\tEno\t\tName\t\tSal\t\tCom Name")
        print("_"*50)
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val,end=" "))
                print()
            except EOFError:
                print("_"*50)
                break