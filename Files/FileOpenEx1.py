#program for demonstrating how to open the filel in "r" mode

try:
    fp=open("kvr2.data","r")
except FileNotFoundError:
    print("File Does Not Exist")
else:
    print("file opened in read mode successfully")
    print("Type of tp=",type(fp))
finally:
    print("_"*50)
    print("I am From Finally Block")
    try:
        print("\tIs File Closed Before Close()=",fp.close())
        fp.close()
        print("\tIs File Closed after close()=",fp.close())
    except NameError:
        print("\tFile Itself Not Opened and No Need To Close")
    finally:
        print("Program Execution Completed")