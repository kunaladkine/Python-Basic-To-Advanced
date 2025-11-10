#program for Demonstrating how to read the file content--read()

try:
    with open("stud2.data","r")as fp:
        filedata=fp.read()
        print("_"*50)
        print(filedata)
        print("_"*50)
except FileNotFoundError:
    print("File Does Not Exist")