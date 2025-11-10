#nested or inner tuple

#-------------------------
#Tupleintuple
t1=(10,"Rossum",(10,20,40),(39,45,55),"RS",2+3j)
print(t1)
print(t1[0])
print(t1[2])
print(t1[4])
print(t1[-3])
print(t1[2][0])         #index of inner tuple element value


#-------List in Tuple-----------------
t2=(10,"Rossum",[-1,0,9,60,45],[20,44,88],"OCET")
print(t2,type(t2),id(t2))
print(t2[2],id(t2))
print(t2[2].sort())

