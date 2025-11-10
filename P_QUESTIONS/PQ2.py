# Problem Statement:
# Accept the student’s name, roll number, and marks in 5 subjects (out of 100).
# Store all marks in a list.
# Calculate:
# Total Marks
# Average
# Percentage
# Use typecasting to convert total marks (float) into integer.
# Use relational and logical operators to:
# Check whether the student passed in all subjects (pass mark = 35)
# Check for scholarship eligibility:
# If average ≥ 90 → Eligible for 100% Scholarship
# If average ≥ 75 and < 90 → Eligible for 50% Scholarship
# Otherwise → Not eligible
# Use assignment operators to update and store the scholarship percentage.
# Print all details including marks list, result, and scholarship.

# Accept student name and roll number
name = input("Enter Your Name : ")
roll_number = int(input("Enter Your Roll No : "))

# Accept marks of 5 subjects
mark = []
for i in range(5):
    m = float(input(f"Enter Marks of Subject {i+1} : "))
    mark.append(m)

# Display entered marks
print("\n----- Student Report -----")
print("Name        :", name)
print("Roll Number :", roll_number)
print("Marks       :", mark)

# Calculate total, average, percentage
total = sum(mark)
average = total / len(mark)
percentage = (total / 500) * 100

# Display results
print("Total Marks :", total)
print("Average     :", average)
print("Percentage  :", percentage, "%")

