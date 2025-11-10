#program for demonstrating default arguments

def dispstudinfo(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("_"*50)
print("\tSNO\tName\tMarks\tCourse")
print("_"*50)
dispstudinfo(100,"Rs",77)   #function call wwith positional args
dispstudinfo(101,"TR",33)
dispstudinfo(102,"RS",22,"JAVA")
dispstudinfo(103,"EW",55,"POLItics")