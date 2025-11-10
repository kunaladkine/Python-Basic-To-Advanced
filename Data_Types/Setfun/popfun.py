#syntax : SetObj.pop()
#this function is used removing arbirtary element.

#ex1
s1={10,20,30,40,50,60,70,80,90}
print(s1.pop())                 #removes any random , any element from the set
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1)
print(s1.pop())

#----------------

print(set().pop())          #gives the KeyError: 'pop from an empty set

