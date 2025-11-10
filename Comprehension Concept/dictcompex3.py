print("Enter List of Values Separated by Comma : ")
lst=[float(val) for val in input().split(",")]
#cal squares for every value of lst
d={val:val**2 for val in lst}
print("_"*50)
print("\tNumbers\t\tSquares")
print("_"*50)
for k,v in d.items():
    print("\t{}\t\t\t{}".format(k,v))
print("_"*50)