#Student Marks Calculator
#arithmeticex5.py

sub1=int(input("Enter Marks : "))
sub2=int(input("Enteer Marks : "))
sub3=int(input("Enteer Marks : "))
sub4=int(input("Enteer Marks : "))
sub5=int(input("Enteer Marks : "))
print("You Enters Marks = {},{},{},{},{}".format(sub1,sub2,sub3,sub4,sub5))
print("-"*60)
total_marks=sub1+sub2+sub3+sub4+sub5
print("\t\tTotal Marks is :{} ".format(total_marks))
ave_mark=total_marks/5
print("\t\tAverage Marks = {}".format(ave_mark))
per_marks=(total_marks/500)*100
print("\t\tPercentage of Students is = {}%".format(per_marks))

