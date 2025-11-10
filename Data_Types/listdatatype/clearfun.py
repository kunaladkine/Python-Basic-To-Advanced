#Syntax Listobj.clear()
#this function removes all the elements from list object.
#when we call this function on empty list object then we get none as result or no result

# Example 1
lst=[10,"Rossum",34.56,"Python",2+3j]
print(lst)
# len(lst)
print(len(lst))
lst.clear()         #it will remove all the elements from the list
print(lst)          #it will show blank list

print([].clear())   #it will print the none

print(list().clear())       #it will print the none value 