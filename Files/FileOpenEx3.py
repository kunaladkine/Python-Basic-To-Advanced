#program for demonstrating how to open the file in "r" mode

with open("kvr1.data","r") as fp:
    print("_"*50)
    print("File Opened in REad Mode Successfully")
    print("Type of tp=",type(fp))
    print("_"*50)
    print("\tIs File Closed withing 'with open() as' Indentation=",fp.closed)
    print("="*50)
    print("\tIs File Closed after 'with open() as' Indentation=",fp.closed)