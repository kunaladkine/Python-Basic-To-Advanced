
def hike(sal):
    return sal+sal*50/100

#main program
print("Enter List of Old Salaries of Employee:")
oldsals=[float(sal) for sal in input().split() if float(sal)>0]
newsals=list(map(hike,oldsals))
print("_"*50)
print("old Salary List\t\tNew Salary List")
print("_"*50)
for old,new in zip(oldsals,newsals):
    print("\t{}\t\t\t{}".format(old,new))
print("_"*50)
