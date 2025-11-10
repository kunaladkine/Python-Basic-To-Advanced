#program for creating csv file with dict in list
import csv
colname=["PID","PNAME","PRICE"]
records=[{"PID":100,"PNAME":"KitKat","PRICE":20.25},
        {"PID":200,"PNAME":"Catburry","PRICE":30.25},
        {"PID":300,"PNAME":"ChacoPie","PRICE":50.45},
        {"PID":400,"PNAME":"MangoByte","PRICE":10.00}]
with open("product.csv","a")as fp:
    csvdwr=csv.DictWriter(fp,fieldnames=colname)
    csvdwr.writeheader()
    csvdwr.writerows(records)
    print("CSV File Created --Verify")