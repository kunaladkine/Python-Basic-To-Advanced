#syntax : Listobj.append(value)
#this function is used for adding a new value at the end of list object

# Example1
lst1=[10,"Rosum",34.33]
print(lst1,type(lst1),id(lst1))
lst1.append("python")           #python is added to the last element
print(lst1)

lst1.append(25)             #we can add only one element at a time
print(lst1)

# example 2
lst2=[]
lst2.append("data")
print(lst2)
lst2.append(22)
print(lst2)
print(len(lst2))
