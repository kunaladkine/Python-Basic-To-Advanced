# Accept total number of days and convert into years, weeks, and days.
#arithmeticex6.py
days=int(input("Enter Number of Days:"))
print(f"You Entered Days ={days}")

#days into years
years=int(days/365)
rem_days = days % 365
rem_days1=int(rem_days)
#days into week
week=int(days/7)
rem_week=week%7
rem_week1=int(rem_week)

print("Equivalent Time:")
print("Years :", years,"Remaining Days : ", rem_days1)

print("Weeks :", week,"Remaining Week : ",rem_week1)
print("Days  :", days)