#program for demonstrating positional arguments
#pssargsex1.py

def dispstudinfo(sno,snmae,marks):
    print("\t{}\t{}\t{}".format(sno,snmae,marks))

#main program
print("_"*50)
print("\tSNO\tName\tMarks")
print("_"*50)
dispstudinfo(100,"RS",44)   #function call with positional args
dispstudinfo(101,"KV",38)   #function call with positional args
dispstudinfo(marks=33,snmae="KR",sno=102)   #function call with keyword args
dispstudinfo(103,marks=49,snmae="RA")   #function call with positional argswith keywrod args
# dispstudinfo(marks=49,snmae="RA",104)   #it gives syntax error