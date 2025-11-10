#program for demonstrating positional arguments

def dispstudinfo(sno,sname,marks,crs):
    print("\t{]\t{}\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("_"*50)
print("\tSNO\tName\tMarks\tCourse")
print("_"*50)
dispstudinfo(100,"RS",44,"PYTHON")      #function call with positional args
dispstudinfo(101,"KV",33,"PYTHON")
dispstudinfo(102,"ES",33,"PYTHON")


