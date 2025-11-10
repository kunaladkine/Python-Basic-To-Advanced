#using relational operator

lst1=[10,"RS",30.33]
print(lst1,id(lst1))
lst2=lst1       #DEEP copy
print(lst2,id(lst2))

#------------------
#Shallow Copy
lst3=lst1.copy()            #shallow Copy
print(lst3,id(lst3))

print(id(lst1)==id(lst2))   #id is same
print(id(lst1)!=id(lst2))   #is not use
print(id(lst1)==id(lst3))   #id is diffent
print(id(lst1)!=id(lst3))   #id is different and is not use
