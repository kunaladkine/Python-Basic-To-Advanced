even=lambda x: x>0

#main program
print("Enter list of Values Separated by Space :")
lst=[float(val) for val in input().split()]
print("List of Values :",lst)
pslist=list(filter(even,lst))
print("Positive Values List is : ",pslist)