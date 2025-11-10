#program for Listing the Files from any Folder---we use listdir()
#OSListFilesEx1.py
import os
FileNamesList=os.listdir("C:\\Users\\KVR\\9am Files Examples")
print("----------------------------------------------")
print("Number of Files=",len(FileNamesList))
print("----------------------------------------------")
for filename in FileNamesList:
    print("\t{}".format(filename))
print("----------------------------------------------")