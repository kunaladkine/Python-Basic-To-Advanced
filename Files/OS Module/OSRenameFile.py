#program for renaming a File Name--we use rename()
#OSRenameFile.py
import os
try:
    os.rename("D:\\PACK2\\MathsInfo.py","D:\\PACK2\\mi.py")
    print("File Renamed ")
except FileNotFoundError:
    print("Source Folder Does not Exist")