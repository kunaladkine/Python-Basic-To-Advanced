#program for Removing the File Name
#OSRemoveFileName.py
import os
try:
    os.remove("D:\\PACK2\\icici.py")
    print("File Name Removed Sucessfully")
except FileNotFoundError:
    print("File Does Not Exist")