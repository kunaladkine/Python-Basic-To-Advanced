#syntax : SetObj.isdisjoint(SetObj2)
#this function returns True provided there are no common elements in both Setobj1 and SetObj2
#this function returns False provided there is at least One common element in Both SetObj1 and SetObj2\

#----------------------
s1={10,20,30}
s2={20,30,40}
print(s1.isdisjoint(s2))        #Because is the some element same in the set s1,and s2
print(s1)

s3={50,60,70}
print(s1.isdisjoint(s3))           #Print True because no same element

#----------------------
#IMP Question
s="WHY"
print(set(s).isdisjoint(set("AEIOU")))      #No Any SAme Element

print(set("apple").isdisjoint(set("AEIOU")))        #same element

#--------------------
#empty set of empty set is True
print(set().isdisjoint(set()))

#---------------------

print(set().isdisjoint({10,20,30}))     #empty set is empty and another set ccontains element but not in the previous so it will print true

