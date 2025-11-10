s1={10,20,30,40,10,20,60,10}
print(s1)           #it will print only unique values, removes the duplicatoin

s=set()
print(s,type(s))
print(len(s))

print(len(s1))      #it will take only unique values


#ex 2
s2="MISSISSIPPI"
print(s2,type(s2),id(2))
s3=set(s2)
print(s3,type(s3),id(s3))

#ex3
#int to set
a=10
print(a,type(a),id(a))
s5=set([a])
print(s5,type(s5),id(s5))

#converting to set
b=10.33
print(b,type(b))
s6=set((b,))
print(s6)