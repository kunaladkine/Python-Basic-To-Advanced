#program for adding two list elementss

def addtwolists(v1,v2):
    return v1+v2

#main program
lst1=[float(val) for val in input("Enter List Values:").split()]
lst2=[float(val) for val in input("Enter 2nd List Values:").split()]

#add two list elements
lst3=list(map(addtwolists,lst1,lst2))
print("_"*50)
print("\tList1\t\tList2\t\tList3")
print("_"*50)
for v1,v2,v3 in zip(lst1,lst2,lst3):
    print("\t{}\t\t{}\t\t{}".format(v1,v2,v3))
print("_"*50)