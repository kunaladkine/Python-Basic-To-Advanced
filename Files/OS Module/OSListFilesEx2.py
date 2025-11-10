#program for Listing the Python Files from any Folder---we use listdir()
#OSListFilesEx2.py
import os
FileNamesList=os.listdir("C:\\Users\\KVR\\9am Files Examples")
print("----------------------------------------------")
print("Number of Files=",len(FileNamesList))
print("----------------------------------------------")
nop=0
for filename in FileNamesList:
    if(filename.endswith(".py")):
        print("\t{}".format(filename))
        nop+=1
print("----------------------------------------------")
print("Number of Python Files=",nop)
print("----------------------------------------------")