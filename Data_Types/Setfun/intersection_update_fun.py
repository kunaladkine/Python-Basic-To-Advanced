#Syntax : SetObj1.intersection_update(Setobj2)
#this function obtais commong elements from SetObj1 and SetObj2 and those elements placed in SetObj1 Itself.

s1={10,20,30,40,50}
s2={30,40,50}
s1.intersection_update(s2)      #it will take common element and put in itself s1
print(s1)

#-------------------------

s3={10,20,30}
s4={50,60}
s3.intersection_update(s4)      #print empty set because no common element
print(s3)

