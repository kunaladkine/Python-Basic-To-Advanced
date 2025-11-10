mark=int(input("Enter Your Marks:"))
if(mark<0):
    print("{} is Invalid Marks.".format(mark))
elif(mark>=90 and mark<=100):
    print("Marks : {} (Grade A+)".format(mark))
elif(mark>=80 and mark<=89):
    print("Marks : {} (Grade A)".format(mark))
elif(mark>=70 and mark<=79):
    print("Marks : {} (Grade B)".format(mark))
elif(mark>=60 and mark<=69):
    print("Marks : {} (Grade C)".format(mark))
elif(mark>=50 and mark<=59):
    print("Marks : {} (Grade D)".format(mark))
elif(mark>=35 and mark<=49):
    print("Marks : {} (Grade E)".format(mark))
elif(mark<35):
    print("Marks : {} (Fail)".format(mark))
elif(mark>100):
    print("{} is Invalid Marks.".format(mark))
else:
    print("Program Executed Complete.")