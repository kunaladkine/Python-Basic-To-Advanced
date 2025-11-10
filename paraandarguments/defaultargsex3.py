#program for demonstratinng default arguments

def dispstudinfo1(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

def dispstudinfo2(sno,sname,marks,crs="Java",cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("_"*50)
print("\tSNO\tName\tMarks\tCourse")
print("_"*50)
dispstudinfo1(100,"RS",49.44)
dispstudinfo1(101,"RE",55.88)
dispstudinfo2(102,"KV",44.33)
dispstudinfo1(102,"WS",99.22)
dispstudinfo2(104,"Rs",44.66,cnt="USA",crs="HTML")