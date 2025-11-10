#progaram for creating csv filel with list in list
import csv #step-1
colnames=["TNO","TNAME","SUBJECT"]      #step-2
records=[[100,"Rajesh","C"],
         [200,"Ramesh","C++"],
         [300,"Rakesh","Python"]]
with open("teacher.csv","a")as fp:  #step-4
    csvwr=csv.writer(fp)    #step-5 here csvwr is and object of <class, csv.writer>
    #here csvwr obj3ct contains two functions 1. writerow() 2. writerows()
    csvwr.writerow(colnames) #step-6 saaving header or colnames to scv file
    csvwr.writerows(records)    #step-7 saving records to the csv file
    print("CSV File Created ----Verify")
