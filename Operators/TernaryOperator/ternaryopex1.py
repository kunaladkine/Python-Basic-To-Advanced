#Syntax : LHSvarname=Expr1 if Test condition else Expr2

#program to accepting any value and decide whether it is plaindrome or not

value=input("Enter any Value :")
res="Palindrome" if value==value[::-1] else "Not Palindrome"
print("\t{} is {}".format(value,res))