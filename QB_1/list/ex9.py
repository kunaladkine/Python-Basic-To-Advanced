# Python program to print all positive numbers in a range

lst=[10,20,45,78,9,-8,-9,65,-4,-5,-7,88]
for val in lst:
    if(val>0):
        print(val)


pvale=[val for val in lst if(val>0)]
print(pvale)