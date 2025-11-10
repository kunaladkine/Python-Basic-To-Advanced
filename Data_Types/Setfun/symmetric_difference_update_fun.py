#Syntax: SetObj1.symmetric_difference_update(SetObj2)
#this function removes the common elements from Setobj1 and SetObj2 and takes remaning elements from both SetObj1 and SetObj2 and place them in SetObj1 Itself

s1={10,20,30}
s2={20,30,40}

s1.symmetric_difference_update(s2)      #common elements remove take further elements
print(s1)

#---------------------

s1.symmetric_difference_update({10,20,60,70})
print(s1)