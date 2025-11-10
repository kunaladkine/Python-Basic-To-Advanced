# Great! Here's an extended version of the same program that:
# ✅ Accepts marks in Math, Science, and English
# ✅ Uses only if statements (no elif, no else)
# ✅ Prints "Pass" or "Fail" for each subject
# ✅ Assigns grades based on marks:
# 90+ → Grade A
# 75–89 → Grade B
# 60–74 → Grade C
# 35–59 → Grade D
# <35 → Fail
# ✅ If all subjects are passed, prints "You Passed All Subjects with Grades"
# ✅ Also prints "Program Executed Successfully"

math=float(input("Enter Your Marks:"))
science=float(input("Enter Your Marks:"))
english=float(input("Enter Your Marks:"))

#math marks

if math>=90:
    print("Math : Pass (Grade A)")
if math>=75 and math<=89:
    print("Math : Pass (Grade B)")
if math>=60 and math<=74:
    print("Math : Pass (Grade C)")
if math>=35 and math<=59:
    print("Math : Pass (Grade D)")
if math>=0 and math<=35:
    print("Math : Fail")

#science
if science>=90:
    print("Science : Pass (Grade A)")
if science>=75 and science<=89:
    print("Science : Pass (Grade B)")
if science>=60 and science<=74:
    print("Science : Pass (Grade C)")
if science>=35 and science<=59:
    print("Science : Pass (Grade D)")
if science>=0 and science<=35:
    print("Science : Fail")

#englsih
if english>=90:
    print("English : Pass (Grade A)")
if english>=75 and english<=89:
    print("English : Pass (Grade B)")
if english>=60 and english<=74:
    print("English : Pass (Grade C)")
if english>=35 and english<=59:
    print("English : Pass (Grade D)")
if english>=0 and english<=35:
    print("English : Fail")

if math>=35 and science>=35 and english>=35:
    print("🎉 You Passed All Subjects with Grades ")

print("Program Executed Successfuly...!")


