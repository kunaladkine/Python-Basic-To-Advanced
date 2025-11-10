#program for renaming a Folder--we use rename()
#OSRenameFolder.py
import os
try:
    os.rename("KVR","HYD")
    print("Folder Renamed")
except FileNotFoundError:
    print("Source Folder Does not Exist")