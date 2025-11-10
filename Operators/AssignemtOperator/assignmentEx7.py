#program for reading two values and swaap them
#assignmentEx7.py

a,b=int(input("Enter Value of a: ")), int(input("Enter Value of b: "))
print("-"*50)
print("\t\tOriginal Val of a =",a)
print("\t\tOriginal Value of b=",b)
print("-"*60)

#swapping by using single line assignment
a=a*b
b=a//b
a=a//b
print("\tSwapped val of a=",a)
print("\tSwaapped val of b=",b)