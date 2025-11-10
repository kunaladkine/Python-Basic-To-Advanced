#program for reading the values from key board by using list comprehension

print("Enter List of Values separated by space  :")
lst1=[float(val) for val in input().split()]
print("List of Values=",lst1)