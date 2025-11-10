val1=float(input("Enter 1st Value :"))
val2=float(input("Enter 2nd Value :"))
val3=float(input("Enter 3rd Value :"))

#check for smaller no
if val1<=val2 and val1<=val3 and not(val1==val2 and val1==val3):
    print(f"{val1} is Smaller.")
if val2<=val3 and val2<=val1 and not (val2==val3 and val2==val1):
    print(f"{val2} is Smaller.")
if val3<=val1 and val3<=val2 and not(val3==val1 and val3==val2):
    print(f"{val3} is Smaller.")

#check for equality.
if val1==val2==val3:
    print("All Values are Equal.")
if val1==val2 and val1!=val3:
    print(f"{val1} and {val2} Are Same.")
if val1==val3 and val2!=val3:
    print(f"{val1} and {val3} are Same.")
if val2==val3 and val2!=val1:
    print(f"{val2} and {val3} are Same.")

print("Program Executed Successfully.")