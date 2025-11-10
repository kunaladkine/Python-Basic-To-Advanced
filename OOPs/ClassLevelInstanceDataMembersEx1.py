#program for strig sno,sname, marks and crss for all the students by using classes and object

class Student:
    crs="PYTHON" #here crs is called class level data member way -1

#main program
#specify the anotheer class level data member city
Student.city="Hyd"
#Create Multiple Object os Student Class
s1=Student()
s2=Student()
#Read and Place the Instance Data members in s1 Object.
s1.sno=int(input("Enter First Student Number:"))
s1.sname=input("Enter First Student Name:")
s1.marks=float(input("Enter First Student Marks:")) # here sno,sname and marks are called Instance Data Members
print("---------------------------------------------------------")
#Read and Place the Instance Data members in s2 Object.
s2.sno=int(input("Enter Second Student Number:"))
s2.sname=input("Enter Second Student Name:")
s2.marks=float(input("Enter Second Student Marks:")) # here sno,sname and marks are called Instance Data Members
#Display the Content of s1 Object
print("---------------------------------------------------------")
print("First Object s1 Data ")
print("\tStudent Number=",s1.sno)
print("\tStudent Name=",s1.sname)
print("\tStudent Marks=",s1.marks)
print("\tSTUDENT COURSE=",Student.crs)
print("\tSTUDENT CITY=",Student.city)
print("------------------------------------------------------------")
#Display the Content of s2 Object
print("Second Object s2 Data ")
print("\tStudent Number=",s2.sno)
print("\tStudent Name=",s2.sname)
print("\tStudent Marks=",s2.marks)
print("\tSTUDENT COURSE=",Student.crs)
print("\tSTUDENT CITY=",Student.city)
print("----------------------------------------------------------")