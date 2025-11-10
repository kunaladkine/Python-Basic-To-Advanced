# Python program to print negative numbers in a list
print("Enter List of Elements Separated By Comma:")
lst=[float(val) for val in input().split()]
nvalue=list(filter(lambda val:val<0,lst))
print("The Negative List is :",nvalue)


for val in lst:
    if(val<0):
        print(val,end=" ")
    else:pass
