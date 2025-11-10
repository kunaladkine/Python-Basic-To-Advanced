#program for Demonstrating how to read the file content --- readlines()

try:
    with open("stud2.data","r") as fp:
        filedata=fp.readline()
        print("_"*50)
        for record in filedata:
            print(record,end="")
        print("_"*50)
except FileNotFoundError:
    print("File Does Not Exist")