a = []

# Step 1: Take initial user input
b = input("Enter Your Name: ")
c = int(input("Enter Your Age: "))
d = input("Enter Your Course: ")

# Step 2: Add data to list
a.append(b)
a.append(c)
a.append(d)

print("\nInitial Data:", a)

# Step 3: Show menu
print("\nWhat do you want to do?")
print("1. Update Name")
print("2. Update Course")
print("3. Remove Age")
print("4. Show Final List")

choice = int(input("Enter your choice (1-4): "))

# Step 4: Perform action based on user choice
if choice == 1:
    new_name = input("Enter your new name: ")
    a[0] = new_name  # index 0 = name
elif choice == 2:
    new_course = input("Enter your new course: ")
    a[2] = new_course  # index 2 = course
elif choice == 3:
    a.pop(1)  # index 1 = age
    print("Age removed.")
elif choice == 4:
    print("Final Data:", a)
else:
    print("Invalid Choice")

# Step 5: Show updated list
print("Updated List:", a)
