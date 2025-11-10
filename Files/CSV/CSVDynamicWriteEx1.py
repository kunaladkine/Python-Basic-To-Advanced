#program for Creating CSV File Dynamically
#CSVDynamicWriteEx1.py
import csv # Step-1
noc=int(input("Enter How Many Columns u Have:"))
#Step-2: Get the Colnames Dynamically
if(noc<=0):
    print("\t{} is Invalid input".format(noc))
else:
    colnames=[] # empty list for placing dynamic Column names
    for i in range(1,noc+1):
        colname=input("Enter {} Column Name:".format(i))
        colnames.append(colname)
    else:
        #Step-3: Get the Records Dynamically.
        nor=int(input("Enter How Many Records u have:"))
        if(nor<=0):
            print("\t{} is invalid Number of Records".format(nor))
        else:
            records=[] # outer empty list for adding inner list-record
            for i in range(1,nor+1):
                print("-"*50)
                print("Enter {} Record Details".format(i))
                print("-" * 50)
                record=[] # Inner List for adding single record values
                for d in range(len(colnames)): # Inner loop--gets record values for single record
                    recval=input("\tEnter Value for {}:".format(colnames[d]))
                    record.append(recval)
                else: # Inner loop
                    records.append(record)
                    print("-" * 50)
            else:#Outer loop
                print("-" * 50)
                #Step-4: accept CSV File Name with an extension .csv
                while(True):
                    csvfile=input("Enter Any File Name with an extension .csv:")
                    if(csvfile.endswith(".csv")):
                        break
                #Step--4--Choose the CSV File and open in w mode and save records
                with open("E:\\KVR-PYTHON-9AM\\CSV\\NOTES\\"+csvfile,"a") as fp:
                    #Step-5: Create an object writer objct
                    csvwr = csv.writer(fp)
                    #Step-6: write the column names to csv file
                    csvwr.writerow(colnames)
                    #Step-7: write records to the csv file
                    csvwr.writerows(records)
                    print("CSV File Created Dynamically--verify")