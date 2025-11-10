#Syntax : Listobj1.extend(Listobj2)
#this functioin is used for merging the content of listobj2 with listobj1

# ex1

lst1=[10,20,30]
lst2=["R","S","k"]
lst3=[1.2,1.3,1.4]
print(lst1)
print(lst2)
print(lst3)

# lst1.extend(lst2)
# print(lst1)

# lst1.extend(lst3)
# print(lst1)

# Or

lst1=lst1+lst2+lst3
print(lst1)