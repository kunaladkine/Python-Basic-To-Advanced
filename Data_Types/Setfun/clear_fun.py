#syntax : SetObject.clear()
#This function removes all the elements from set object.
#when we call this function on empty set object then we get space Or None as result

#------------------------
s1={10,20,30,40,50,60}
print(len(s1))

s1.clear()
print(len(s1))

#-------------------
set().clear()                   #it will print none in command promt
print(set().clear())            #it will print 'None'

