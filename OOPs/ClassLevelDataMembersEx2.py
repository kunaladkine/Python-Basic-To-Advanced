#program for Demonstrating class level data members

class Student:pass

#main program
Student.crs="PYTHON"    #here crs is called class level data member in student class
Student.city="Berlin" #here city is called class level data member in student class

#accessing the class level data member by using class name
print("Student Course=",Student.crs)
print("Student City=",Student.city)