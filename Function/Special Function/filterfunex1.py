#program for reading list of numerical values and a filter only +ve values

def even(val):
    if(val>0):
        return True
    else:
        return False

#main program
print("Enter List of Values Separated By Space :")
lst=[float(val) for val in input().split()]
print("List of values =")
print(lst)
fobj=filter(even,lst)
pslist=list(fobj)
print("List of +VE Values")
print(pslist)