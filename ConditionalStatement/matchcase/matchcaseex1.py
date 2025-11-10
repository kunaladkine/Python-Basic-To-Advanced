#arithmetic operation program
print("---------Arithmetic Operation------------")
print("\t\t1. Addition")
print("\t\t2. Substraction")
print("\t\t3. Multiplication")
print("\t\t4. Division")
print("\t\t5. Floor Division")
print("\t\t6. Modulo")
print("\t\t7. Exponentiation")
print("\t\t8. Exit")
ch=int(input("Enter Ur Choice: "))
match(ch):
    case 1:
        print("Enter Two Values for Addition :")
        a,b=float(input("Enter Value:")),float(input("Enter Value"))
        print("\t\tSum({},{}) = {}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Substraction :")
        a,b=float(input("Enter Value :")),float(input("Enter Value"))
        print("\t\tSub({},{}) = {}".format(a, b, a - b))
    case 3:
        print("Enter Two Value for Multiplication :")
        a,b=float(input("Enter Value :")),float(input("Enter Value"))
        print("\t\tMul({},{}) = {}".format(a, b, a*b))
    case 4:
        print("Enter Two Values for Divison:")
        a,b=float(input("Enter Value:")),float(input("Enter Value"))
        print("\t\tDiv({},{}) = {}".format(a, b, a / b))
    case 5:
        print("Enter Two Value for Floor Divison: ")
        a,b=float(input()),float(input())
        print("\t\tFloordiv({},{}) = {}".format(a, b, a//b))
    case 6:
        print("Enter Two Values for Modulo Division :")
        a,b=float(input()),float(input())
        print("\t\tMod({},{}) = {}".format(a, b, a%b))
    case 7:
        print("Enter Two Value for Exponentiation :")
        a,b=float(input("Enter Base:")),float(input("Enter Power:"))
        print("\t\tPow({},{}) = {}".format(a, b, a**b))
    case 8:
        print("Thx for using Program.")
    case _:
        print("Ur Selection of Operation wrong - try again.")
print("Program Exectution Completed.")