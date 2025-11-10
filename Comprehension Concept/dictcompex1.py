#program 1

lst=[10,20,22,11,27,25,-35,-8,-96]
d={val:val**2 for val in lst}
print("_"*50)
print("\tNumber\t\tSquare")
print("_"*50)
for k,v in d.items():
    print("\t{}\t\t\t{}".format(k,v))
print("_"*50)