#Syntax : ListObj.reverse()
#this function is used for obtaing reversed elements of list and place the reversed elements in listobj itself

#reversing the elements is nothig but getting back to front and vice versa.

# Ex1

lst1=[10,"rossum",2+3j,30.33]
print(lst1,id(lst1))
lst2=lst1.reverse()
print(lst2)     #it will print the none
print(lst1,id(lst1))        #list will eversed elements in listob itself


# ex2

data=[10,20,30,40,50]
print(data,id(data))
a=data.reverse()
print(data)