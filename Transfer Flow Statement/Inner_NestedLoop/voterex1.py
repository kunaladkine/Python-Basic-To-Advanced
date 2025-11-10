#program for accepting age of cititzen an decide whetehr the citizen is eligible to vote or not

age=int(input("Enter Age of Cititizen:"))
if(age<18) or (age>100):
    print("\t {} years citizen is not eligible to Vote :".format(age))
else:
    print("\t{} Years Citizen is Eligible to Vote.".format(age))