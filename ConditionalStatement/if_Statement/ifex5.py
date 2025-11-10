val1 = float(input("Enter Value 1st : "))
val2 = float(input("Enter Value 2nd : "))
val3 = float(input("Enter Value 3rd : "))

# Only one big value should be printed
if val1 >= val2 and val1 > val3 and not (val1 == val2 or val1 == val3):
    print(f"{val1} is the biggest number.")
if val2 > val1 and val2 >= val3 and not (val2 == val1 or val2 == val3):
    print(f"{val2} is the biggest number.")
if val3 >= val1 and val3 > val2 and not (val3 == val1 or val3 == val2):
    print(f"{val3} is the biggest number.")

# Check for equality cases
if val1 == val2 == val3:
    print("All three values are equal.")
if val1 == val2 and val1 != val3:
    print("Value 1 and Value 2 are equal.")
if val1 == val3 and val1 != val2:
    print("Value 1 and Value 3 are equal.")
if val2 == val3 and val2 != val1:
    print("Value 2 and Value 3 are equal.")

print("Program Executed Successfully.")
