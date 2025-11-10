#program for Creating a Folder--we use  mkdir() of os module
#OSCreateFolder.py
import os
try:
    os.mkdir("KVR")
    print("Folder Created  Sucessfully")
except FileExistsError:
    print("Folder already exist")
except FileNotFoundError:
    print("Root Folder Does not Exist to create Sub Folder")