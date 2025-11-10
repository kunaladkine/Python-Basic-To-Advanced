#program for copying the conteent of one file into another file

def copyfile():
    try:
        srcfile=input("Ente Source File:")
        with open(srcfile,"rt") as rp:
            dstfile=input("Enter Destination File:")
            with open(dstfile,"a") as wp:
                #read the data from source file
                srcfiledata=rp.read()
                #write the srcfile data to destination file
                wp.write(srcfiledata)
                print("Source File Data Copied into Destination File")
    except FileNotFoundError:
        print("Source file Does Not Exist")

#main program
copyfile()