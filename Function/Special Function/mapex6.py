#program for adding two list elements

print("Enter First List of Values :")
lst1=[float(val) for val in input().split()]
print("Enter Second List Values :")
lst2=[float(val) for val in input().split()]
if(len(lst1)>len(lst2)):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0)
elif(len(lst2)>len(lst1)):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)

#add two list elements
lst3=list(map(lambda val1,val2:val1+val2,lst1,lst2))
print("_"*50)
print("\tList1\t\tList2\t\tList3")
print("_"*50)
for v1,v2,v3 in zip(lst1,lst2,lst3):
    print("\t{}\t\t{}\t\t{}".format(v1,v2,v3))
print("_"*50)