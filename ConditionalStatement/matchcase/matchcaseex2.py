#program for implementing all area of different figures
import sys
s="""-----------------------------------
            Area of Different Figures
--------------------------------------
        C. Circle
        S. Square
        R.Rectangle
        T. Triangle
        E. Exit
--------------------------------------
"""
print(s)
ch=input("Enter Ur Chocie:")
match(ch):
    case "C" | "c":
        r=float(input("Enter Radius :"))
        ac=3.14*r**2
        print("\tArea of Circle=",ac)
    case "R" | 'r':
        L=float(input("Enter Length:"))
        B=float(input("Enter Breadth:"))
        ra=L*B
        print("\tArea of Rect=",ra)
    case "S"|'s':
        s=float(input("Enter Side:"))
        sa=s**2
        print("\tArea of Square=",sa)
    case "T"|'t':
        print("Enter the values of Three sides of Triangle:")
        a,b,c=float(input()),float(input()),float(input())
        s=(a+b+c)/2
        ta=(s*(s-a)*(s-b)*(s-c))**0.5
        print("\tArea of Triangle=",ta)
        print("-------------OR--------------")
        b=float(input("Enter Base of Triangel:"))
        h=float(input("Enter Height of Triangle:"))
        ta=(1/2)*b*h
        print("\tArea of Triangle=",ta)
    case "E"|'e':
        print("Thx for using Program :")
        sys.exit()
    case _:
        print("Ur Selection of Operation wrong- try again.")
