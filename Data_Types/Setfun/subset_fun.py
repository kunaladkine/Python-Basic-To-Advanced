#Syntax : SetObj.issubset(SetObj2)
#This Function returns True Provided All the Elements of SetObj Present in SetObj2 Otherwise returns False.

s1={10,20,30,40}
s2={10,20}
s3={15,25,35,45}

print(s2.issubset(s1))          #Return True it elements present
print(s1.issubset(s2))

print(s2.issubset(s3))

#----------------

print(set().issubset(set()))            #empty set of empty set is true , empty set

#-----------------

print(set().issubset({10,20,30})) #PResent in elements in set