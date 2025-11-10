#program for adding new reocrd to existing csv file
import  csv
record=[600,"Ram","DSA"]    #new Record
with open("teacher.csv","a")as fp:
    csvwr=csv.writer(fp)
    #here csvwr object contains two functions 1. writerow() 2. writerows()
    csvwr.writerow(record)
    print("Record added to csv file --- verify")