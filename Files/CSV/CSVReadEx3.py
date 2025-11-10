#program for Reading CSV File Data by using TextIOWrapper object
with open("student.csv","r")as fp:
    csvfiledata=fp.read()
    print("_"*50)
    print("CSV File Data")
    print("_"*50)
    print(csvfiledata)
    print("_"*50)