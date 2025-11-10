#program for displaying the conteent of any file name

try:
    filename=input("Enter the File Name to View its Content:")
    with open(filename) as fp:
        filedata=fp.read()
        print("_"*50)
        print(filedata)
        print("_"*50)
except FileNotFoundError:
    print("File Does not Exist")