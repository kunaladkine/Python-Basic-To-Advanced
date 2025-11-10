#program for readin list of numerical values ad filter only +ve values

def even(val):
    return val>0

#main program
print("Enter List of Values Separated By Space:")
lst=[float(val) for val in input().split()]
print("List of Values :",lst)
pslist=list(filter(even,lst))
print("List of +ve Values:",pslist)