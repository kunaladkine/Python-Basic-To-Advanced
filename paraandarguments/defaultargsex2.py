#program for demonstrating default arguments

def dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("_"*50)
print("\tSno\tName\tMarks\tCourse\tCity")
print("_"*50)
dispstudinfo(100,"Rs",35.33)        #function call with positional args
dispstudinfo(101,"RT",88.44)
dispstudinfo(102,"DR",44.33)
dispstudinfo(103,"EW",99.99,"JAVA","USA")
dispstudinfo(104,"WW",22.44,cnt="USA",crs="HTML")   #function call with positional args with keyword args
