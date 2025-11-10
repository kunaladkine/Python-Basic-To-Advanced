#syntax :  SetObj3=SetObj1.difference(SetObj2)
#This function removes the common elemetns from SetObj1 and SetObj2 and takes remaining elements from SetObj1 and place them in SetObj3.

s1={10,20,30,40,50}
s2={20,20,40,60}
s3=s1.difference(s2)            #removes the same elements
print(s3)

#---------------

print({10,20,30,40}.difference({10,20,30}))         #same element remove

#-----------

print(set("RADAR").difference("NISSOR"))
