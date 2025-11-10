# Write a Python program using the ternary operator to check whether a number entered by the user is even or odd.

value=int(input("Enter Your Int Value : "))

res="Even No" if value%2==0 else "Odd No"
print("{} is The {}".format(value,res))

