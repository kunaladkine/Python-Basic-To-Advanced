#program for reading file using csv module
#csv.reader() -----reader calss object.

import csv
with open("student.csv","r")as fp:
    csvr=csv.reader(fp)
    for record in csvr:
        for val in record:
            print("{}".format(val),end="\t")
        print()