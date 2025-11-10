#program for reading only +ve values from key baord by using list comprehension

print("Enter List of Numerical Values separated by space :")
lst1=[float(val) for val in input().split() if float(val)>0]
print("List of Values=",lst1)