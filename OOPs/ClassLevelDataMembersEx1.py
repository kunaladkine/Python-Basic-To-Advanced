#program for Demonstrating Class Level Data Members

class Student:
    crs="PYTHON"        #here crs is called class level data member
    city="HYD"          #here city is called class level data member

#main program
#accessign the class level data members by using class name
print("Student Course=",Student.crs)
print("Student City=",Student.city)