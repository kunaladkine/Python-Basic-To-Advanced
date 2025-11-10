#program for Demonstrating How to Open the File in "w" mode
#FileOpenEx4.py
with open("E:\\KVR-PYTHON-9AM\\FILES\\kvr2.data","w+") as fp:
    print("-"*50)
    print("File Opened in Write Mode sucessfully")
    print("Type of tp=", type(fp))
    print("-" * 50)
    print("\tFile Name=",fp.name)
    print("\tFile Mode=", fp.mode)
    print("\tIs File Closed=",fp.closed)
    print("\tIs File Readable=",fp.readable() )
    print("\tIs File Writable=",fp.writable() )
    print("-" * 50)