#program for reading two values and swaap them
#assignmentEx8.py

a,b=int(input("Enter Value of a: ")), int(input("Enter Value of b: "))
print("-"*50)
print("\t\tOriginal Val of a =",a)
print("\t\tOriginal Value of b=",b)
print("-"*60)

#swapping by using Single Line assigment with Bitwise XOR ( ^)
a=a^b
b=a^b
c=a^b
print("\tSwapped val of a=",a)
print("\tSwaapped val of b=",b)