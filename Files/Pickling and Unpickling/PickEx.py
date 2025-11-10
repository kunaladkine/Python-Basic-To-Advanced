#program for accepting employee values from Key Board and save them as Record in file
#EmpPickEx.py
import pickle
def saveempdata():
    with open("emp.pick","ab") as fp:
        while(True):
            try:
                print("-"*60)
                #accept Employee Values from Key Board
                empno=int(input("Enter Employee Number:"))
                empname=input("Enter Employee Name:")
                empsal=float(input("Enter Employee Number:"))
                print("-" * 60)
                #create an empty list for Placing values employee values
                lst=list()
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                #save Iterable object -lst into the file
                pickle.dump(lst,fp)
                print("Employee Record Saved in File Sucessfully")
                print("-" * 60)
                ch=input("Do u want to Insert Another Employee Record(yes/no):")
                if(ch.lower()=="no"):
                    print("Thx for using this program")
                    break
            except ValueError:
                print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS FOR EMPNO AND SAL")
#Main Program
saveempdata() # Function call