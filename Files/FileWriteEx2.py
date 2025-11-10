#program for demonstrating how to write the data to the file

with open("stud1.data","a")as fp:
    while(True):
        print("-----------------------")
        sno=int(input("Enter Student Number:"))
        sname=input("Enter Student Name:")
        marks=float(input("Enter Student Marks:"))
        print("_"*50)
        fp.write(str(sno)+"\t")
        fp.write(sname+"\t")
        fp.write(str(marks)+"\n")
        print("Data Written to the Files")
        print("_"*50)
        ch=input("Do u want to insert anotheer record(yes/no):")
        if(ch.lower()=="no"):
            print("Thx for uisng program")
            break