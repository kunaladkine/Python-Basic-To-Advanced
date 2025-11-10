#program for adding record to the existing csv file though python lang
#csv writer()----write class object

import csv
record=[400,"KVR",9.4]
with open("emp.csv","a")as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(record)
    print("Record Added to emp.csv file")