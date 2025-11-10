#program for reading the data from keyboard
#and wirte to the file until we say 'stop'

def dynamicwrite():
    with open("hyd1.data","at") as fp:
        print("Enter the Data to the File and press @ to stop:")
        while(True):
            kbddata=input()
            if(kbddata!="@"):
                fp.write(kbddata+"\n")
            else:
                print("Data Writeen To the File")
                break

                #main program
dynamicwrite()