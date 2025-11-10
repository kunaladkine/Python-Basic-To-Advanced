#program for Demonstrating How to Open the File in "x" mode
#FileOpenEx5.py
try:
    with open("kvr2.data","x") as fp:
        print("-"*50)
        print("File Opened in Exclusively Write Mode sucessfully")
        print("Type of tp=", type(fp))
        print("-" * 50)
        print("\tFile Name=",fp.name)
        print("\tFile Mode=", fp.mode)
        print("\tIs File Closed=",fp.closed)
        print("\tIs File Readable=",fp.readable() )
        print("\tIs File Writable=",fp.writable() )
        print("-" * 50)
except FileExistsError:
    print("File Name already Exist")