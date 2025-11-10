print("Enter List of Values Separated By Space:")
lst=[float(val) for val in input().split()]
print("Given List :",lst)
pslist=tuple(filter(lambda val: val>0,lst))
print("List of +ve Values ")
print(pslist)