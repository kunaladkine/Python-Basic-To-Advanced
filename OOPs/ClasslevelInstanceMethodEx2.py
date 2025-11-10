#program for reading the instance data members for an object
#by using instance methods

class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHon"
        cls.getcity()

    @classmethod
    def getcity(cls):
        Student.city="HYD"

    def readstuddata(self, objinfo):
        print("Enter {} Student Information:".format(objinfo))
        self.sno = int(input("\tEnter Student Number:"))
        self.name = input("\tEnter Student Name:")
        self.marks = float(input("\tEnter Student Marks:"))

    def dispstuddata(self, objinfo):
        print("{} Student Information".format(objinfo))
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("\tSTUDENT COURSE=", Student.crs)
        print("\tSTUDENT CITY=", Student.city)


# Main Program
# Create Two objects of Student Object
Student.getcrs()
s1 = Student()
s1.readstuddata("First")
print("---------------------------------------")
s2 = Student()
s2.readstuddata("Second")
print("---------------------------------------")
# display First Student Details
s1.dispstuddata("First")
print("---------------------------------------")
# display Second Student Details
s2.dispstuddata("Second")