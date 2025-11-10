#Syntax  1 : del MutableObject[Index] ---> removes the single element from mutalbe based on index
#syntax 2 : del MutableObject[Start:Stop:Step]  ----> removes the multiple elements from mutable object based on slicing
#Syntax 3 : del MutableImmutableObject -----> it will remove the complete object (Physical existence along with daata

#id will be same in that because mutable
# Example 1

lst=[10,"Rossum",34.56,"python",2+3j]
print(lst,id(lst))

del lst[1]          #it will delet index 1 element
print(lst,id(lst))

del lst[-1]
print(lst,id(lst))          #it will delet -1 index value

lst1=[10,"Rossum",34.56,"Python",2+3j]
del lst1[::2]       #it will print index of 2 positon forward direction element
print(lst1)

del lst1[1:]
print(lst1)

del lst1            #it will delete all the list totally and if we want to print then it will show error
# print(lst1)


# Example 2
s="PYTHON"
# print(s)
# del s[0]  #Typeerror :

del s       # it will delet the s object
print(s)
