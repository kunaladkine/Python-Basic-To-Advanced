#program for Demonstrating how to write the data to the file

sno=200
sname="Rossum"
marks=34.56
with open("stud1.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data Written to thee File")