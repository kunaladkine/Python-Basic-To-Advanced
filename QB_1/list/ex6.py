# Python program to print positive numbers in a list

lst=[float(val) for val in input().split()]
plist=list(filter(lambda val:val>0,lst))
print("The Positive List :",plist)