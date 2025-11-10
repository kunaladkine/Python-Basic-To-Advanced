#program for accepting listoff exisiting sal of employees and
#give 50% hike to employees

def hike(sal):
    return sal+sal*50/100

#main program
print("Enter List of old Salaries of Employes:")
oldsals=[float(sal) for sal in input().split() if float(sal)>0]
print("old salary list")
print(oldsals)
x=map(hike,oldsals)
#convert map object into list type
newsals=list(x)
print("New Salary")
print(newsals)