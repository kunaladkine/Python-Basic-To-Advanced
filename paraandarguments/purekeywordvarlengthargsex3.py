#program for demonstrating the need of keyword variable length arguments
#this program will execute ass it is

def findtotalmarks(rno,sname,cls,**submarks):
    print("_"*50)
    print("\tStudent Number={}".format(rno))
    print("\tStudent Name={}".format(sname))
    print("\tStudent Class={}".format(cls))
    print("_"*50)
    totmarks=0
    print("\tSubject\t\tMarks")
    print("_"*50)
    for subject in submarks:
        print("\t{}\t\t{}".format(subject,submarks.get(subject)))
        totmarks+=submarks.get(subject)
    print("_"*50)
    print("\tTotal Marks={}".format(totmarks))
    print("_"*50)

#main program

findtotalmarks(10,"RS","X",Telgu=80,Hindi=90,English=90,Maths=99,Science=90,Social=89)
findtotalmarks(20,"DR","XII",Snaskrit=99,English=95,Maths=75,Physics=60,chemestry=59)
findtotalmarks(40,"MC","Research")