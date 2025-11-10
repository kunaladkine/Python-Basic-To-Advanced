#program for reading the instance data memberss for an object
#by using Instance Methods
#InstanceMethodEx2.py
class Student:
    def readstuddata(self,objinfo):
        print("Enter {} Student Information:".format(objinfo))
        self.sno=int(input("\tEnter Student Number:"))
        self.name=input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))

    def dispstuddata(self,objinfo):
        print("{} Student Information".format(objinfo))
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))

#main program
#create two objects of student object
s1=Student()
s1.readstuddata("First")
print("_"*50)
s2=Student()
s2.readstuddata("Second")
print("_"*50)
#display first student details
s1.dispstuddata("First")
print("_"*50)
#display second student details
s2.dispstuddata("Second")
print("_"*50)
