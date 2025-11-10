#program for creating CSV File Through Python Lang.

import csv
hname=["Empno","Name","Sal"]
records=[[100,"Rosum",4.5],[200,"KTravis",99.3],[300,"Dennis",5.6]]
#choose the csv file and open it into write mode
with open("emp.csv","w")as fp:
    csvwr=csv.writer(fp)
    #wirte the header Names--
    csvwr.writerows(hname)
    #write the record
    csvwr.writerows(records)
    print("CSV file created dynamically through code--verify")