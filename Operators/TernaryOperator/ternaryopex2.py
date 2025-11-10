#program for accepting two value and find biggest andd check for equality

a=float(input("Enter Value of a : "))
b=float(input("Enter Value of b : "))
res="Value is Big" if a>b else b if b>a else "Both value are equal"
print("Max({},{})={}".format(a,b,res))