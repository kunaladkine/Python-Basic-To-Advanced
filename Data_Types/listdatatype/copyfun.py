#Syntax : listobj2=listobj1.copy()
#thiss function is used for copying the content of one listobject to another list object (implement shallow copy)

# Example of sShallow Copy

lst1=[10,"python",25.99,2+3j]
print(lst1,id(lst1))

lst2=lst1.copy()
print(lst2,id(lst2))

lst1.insert(1,True)
print(lst1)

# Example of Deep copy
#id will be same in that  mutable
lst=[10,"Rossum","Python"]
print(lst,id(lst))

lst3=lst
print(lst3,id(lst3))
