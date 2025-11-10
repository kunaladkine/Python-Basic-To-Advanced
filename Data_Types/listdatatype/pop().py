#syntax : listobj.pop()
#this function alwaays reomves the last element from list object
#id will be same in the pop()
#iterable object list the id same while doing function use
# Example 1

lst=[10,"Rossum",34.23,"Python,2+3j"]
print(lst)
lst.pop()       #removes the last element from the list
print(lst)

lst.pop()
print(lst,id(lst))
lst.pop()           #remove one by one last element while using function
print(lst,id(lst))
lst.pop()       #blank list will be in the last
print(lst)

print(lst,type(lst),id(lst))
lst.pop(0)
print(lst,type(lst),id(lst))   #it will print the error because empty list are not be pop and gives the error

# Example 2
#this all below function give the error  because empty list
[].pop()
list().pop()
print(lst)
