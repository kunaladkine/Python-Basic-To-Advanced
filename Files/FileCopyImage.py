#program for copying the conteent of one file into another file

def copyfileimage():
    try:
        srcfile=input("Ente Source File:")
        with open(srcfile,"rb") as rp:
            dstfile=input("Enter Destination File:")
            with open(dstfile,"wb") as wp:
                #read the data from source file
                srcfiledata=rp.read()
                #write the srcfile data to destination file
                wp.write(srcfiledata)
                print("Source File Data Copied into Destination File")
    except FileNotFoundError:
        print("Source file Does Not Exist")

#main program
copyfileimage()