#program for Demonstrating how to write the data to the file

x={1:"Python",2:"C",3:"C++",4:"Java"}
with open("stud2.data","a")as fp:
    fp.writelines(str(x)+"\n")
    print("Data Written to the File")