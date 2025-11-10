#program for reading the data from csv file
try:
    with open("student.csv","r")as fp:
        csvdata=fp.read()
        print("_"*50)
        print("CSV File Data")
        print("_"*50)
        print(csvdata)
        print("_"*50)
except FileNotFoundError:
    print("File Does Not Exist")