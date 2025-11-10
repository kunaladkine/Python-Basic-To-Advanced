# Write a Python program that takes three exam scores from the user (Math, Science, English). Use only if statements to:
# Print "Pass" for each subject if the score is greater than or equal to 35.
# Print "Fail" for each subject if the score is less than 35.
# If all three scores are 35 or more, print "Congratulations! You passed all subjects."

math=float(input("Enter Your Score:"))
science=float(input("Enter Your Score:"))
english=float(input("Enter Your Score:"))

if math>=35:
    print("Math : Pass")
if math<35:
    print(("Math : Fail"))
if science>=35:
    print("Science : Pass")
if science<35:
    print("Science : Fail")
if english>=35:
    print("English : Pass")
if english<35:
    print("English : Fail")

if math>=35 and science>=35 and english>=35:
    print("Congratulatioins You pass all subect.")
print("Program Executed Successfully.")