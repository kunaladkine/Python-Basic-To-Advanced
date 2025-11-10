import pickle
class StudentRecordRead:
    def readRecord(self):
        try:
            with open("stud.data","rb")as fp:
                print("_"*50)
                while(True):
                    try:
                        record=pickle.load(fp)
                        record.getstuddet()
                    except EOFError:
                        print("_"*50)
                        break
        except FileNotFoundError:
            print("File Does not Exist")

#main program
srr=StudentRecordRead()
srr.readRecord()