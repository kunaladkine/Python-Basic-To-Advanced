#program for Demonstrating the class level method
#classlevelmethodex1.py

class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="Python"    #or Student.crs="python"
    @classmethod
    def getcity(cls):
        Student.city="HYD"

#main program
Student.getcrs()
Student.getcity()
print("Student Course=",Student.crs)
print("Student City=",Student.city)