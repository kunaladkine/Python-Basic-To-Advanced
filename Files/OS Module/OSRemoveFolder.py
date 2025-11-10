#program for Removing the Folder--we use rmdir()
#OSRemoveFolder.py
import os
try:
    os.rmdir("c:\\hyd")
    print("Folder Removed Sucessfully")
except FileNotFoundError:
    print("Folder does not Exist")
except OSError:
    print("U Must ensure that Folder Must be Empty")