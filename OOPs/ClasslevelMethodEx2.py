#program for demonstrating the class level method
#classlevelmethodex2.py

class Student:
    @classmethod
    def getcrs(cls):
        cls.crs="PYTHON"
        cls.getcity()

    @classmethod
    def getcity(cls):
        Student.city="HYD"

#main program
Student.getcrs()
print("Student Course=",Student.crs)
print("Student City=",Student.city)