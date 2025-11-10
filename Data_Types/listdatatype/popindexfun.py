#Syntax  ListObj.pop(index)
#this function is used for removing the value from specified index.
#if the specified index does not exist in list object then we get IndexError

# Example 1

lst1=[10,20,30,40,50,20,30,101,10]
print(lst1)

lst1.pop(3)             #it will remove the 40 at index position 3
print(lst1)

lst1.pop(-3)        #at index position -3 remove the value
print(lst1)