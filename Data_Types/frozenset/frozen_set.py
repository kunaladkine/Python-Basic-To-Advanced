from operator import length_hint

s1={10,20,30,10,20,60,70}
print(s1,type(s1))
fs1=frozenset(s1)
print(fs1,type(fs1))

#-------------------------------
fs2=frozenset()     #empty frozenset
print(fs2,type(fs2))
print(len(fs2))         #length of empty forzenset

#------------------------
s3={10,"RS",33.33,True}
print(s1,type,s3)
s4=frozenset(s3)
print(s4,type(s4))

#-------------------
fs2[0]      #it gives TypeError: 'frozenset' object does not support item assignment

#-----------------

del fs2[2]      #it gives the error

del fs2         #it will delet the all set  #possbile

print(fs2)      #already set delet so NameError Gives


