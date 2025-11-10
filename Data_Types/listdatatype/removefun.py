#Syntax ListObj.remove(value)
#this function is used  for removing the first occurence off sepeciffied value from the object
#if the specified value does not in list object then we get ValueError.
#Moreover, if we call this function on empty list object then we get value error

# Example 1

lst=[10,20,30,10,40,50,30,20,20,50]
print(lst)
len(lst)
lst.remove(20)          #it will remove the value 20 1st comes value
print(lst)
lst.remove(50)          #it will remove the value 50 1st comes value
print(lst)

# Example 2

print(lst.remove(100))      #ValueError
print(lst.remove(3000))   #ValueError
print([].remove((20)))      #Value Error