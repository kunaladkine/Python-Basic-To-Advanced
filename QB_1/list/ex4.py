# Python program to print even numbers in a list

lst=[1,2,3,4,5,6,7,8,9]
evennum=[val for val in lst if val%2==0]
print("Even List Is : ")
print(evennum)


evennum2=tuple(filter(lambda lst:lst%2==0,lst))
print(evennum2)

for i in lst:
    if(i%2==0):
        print(i)
        