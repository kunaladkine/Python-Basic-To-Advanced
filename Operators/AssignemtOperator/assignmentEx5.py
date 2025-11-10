#program for reading two values and swaap them
#assignmentEx4.py

a,b=input("Enter Value of a: "), input("Enter Value of b: ")
print("-"*50)
print("\t\tOriginal Val of a =",a)
print("\t\tOriginal Value of b=",b)
print("-"*60)

#swapping by using single line assignment
t=a
a=b
b=t
print("\tSwapped val of a=",a)
print("\tSwaapped val of b=",b)