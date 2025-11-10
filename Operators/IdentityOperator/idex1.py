#Identity Operator
# types 1. is 2. is not

lst1=[10,"RS",30.33]
print(lst1,id(lst1))

lst2=lst1       #DEEP copy
print(lst2,id(lst2))

print(lst1 is lst2)

print(lst1 is not lst2)

#------------------
#Shallow Copy
lst3=lst1.copy()            #shallow Copy
print(lst3,id(lst3))
print(lst1,id(lst1))        #id is different so not possible 

print(lst3 is lst1)

print(lst1 is not lst3)

