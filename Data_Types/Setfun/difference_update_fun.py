#syntax : SetObj1.difference_update(SetObj2)
#this function removes the common elements from SetObj1 and SetObj2 and takes remaining elements from SetObj1 and place them in SetObj1 Itself.

s1={10,20,30,40}
s2={30,40,50}
s1.difference_update(s2)            #removes common element and put unique element in s1
print(s1)

#--------------
s1.difference_update(s1)            #it will give empty set
print(s1)