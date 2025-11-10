#Syntax : SetObj3=SetObj1.intersection(SetObj2)
#This function obtains common elements from Setobj1 and Setobj2 and those elements placed in SetObj3.

s1={10,20,30,40,50}
s2={30,40,50}

print(s1.intersection(s2))      #it will print common element in both set

s3=s1.intersection(s2)
print(s3)

s4=s1.intersection(s2,{20,30,10,40})
print(s4)
#---------------------
print(set("RADAR").intersection(set("NISSION")))            #no common element in that set


#-------------
print(set("RADAR").intersection(set("RADAR")))      #print common element

#---------------

print(set([10,20,30,40]).intersection([10,20,50,60]))
