#Syntax : SetObj1.issuperset(SetObj2)
#This Function Return True, Provided SetObj contains all the elemetns of SetObj2 otherwise Returned False


#-----------------------

s1={10,20,30,40}
s2={10,20}
s3={15,25,35,10}

print(s1.issuperset(s2))        #return true because value contain in s2

print(s2.issuperset(s3))        #not contain elements in that set

print(s2.issuperset(s1))           #no contain whole elements in that

#---------------------

print(set().issuperset(set()))        #empty set of empty set is true

#---------

print(set().issuperset({10,20,30}))

#--------------------------

print({10,20,30}.issuperset(set()))
