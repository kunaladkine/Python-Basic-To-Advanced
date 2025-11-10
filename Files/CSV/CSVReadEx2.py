#program for reading the data from csv file by using csv module -in  the form dictionary --DicReader()
#Reading Records in CSV File.
import csv
with open("student.csv","r")as fp:
    csvdr=csv.DictReader(fp)
    for record in csvdr:            #record is an object of class dict
        for k,v in record.items():
            print("\t{}--->{}".format(k,v))
        print("_"*50)
 