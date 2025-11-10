#StudentPickWithOOPsEx1.py
from Student import Student
import pickle
class StudentRecordSave:
    def saverecord(self):
        with open("stud.data","ab") as fp:
            while(True):
                try:
                    #accept the student details from KBD
                    print("-"*50)
                    sno=int(input("Enter Student Number:"))
                    sname=input("Enter Student Name:")
                    marks=float(input("Enter Student Marks"))
                    print("-" * 50)
                    #create an object of student
                    so=Student()
                    so.setstuddet(sno,sname,marks)
                    #save student object data into student.data file
                    pickle.dump(so,fp)
                    print("Sudent Object Data Saved in File")
                    print("-" * 50)
                    ch=input("Do u want to Insert another Record(yes/no):")
                    if(ch.lower()=="no"):
                        break
                except ValueError:
                    print("\tDon't enter alnums,strs and symbols-try again")

srs=StudentRecordSave()
srs.saverecord()