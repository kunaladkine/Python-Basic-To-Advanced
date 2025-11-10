#Syntax SetObj3=SetObj1.symmetric_difference(SetObj2)
#this function removes the common elements from SetObj1 and SetObj2 and takes remaing elemetns from both SetObj1 and SetObj2 and placce them in SetObj3

s1={10,20,30,40}
s2={20,30,50,60}

s3=s1.symmetric_difference(s2)          #removes same and take both set element rest
print(s3)

#-------------
print(set("RADAR").symmetric_difference(set("NISSOR")))

#--------------

print({10,20}.symmetric_difference({50,35}))        #both set element are difference so print both sets

