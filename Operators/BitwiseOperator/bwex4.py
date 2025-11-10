#bitwise AND (&) Operator
#Syntax : varname=value&value2

a=5
b=4
print("a&b= ",a&b)

#Comment ANS
A. True
B. False

a=5
b=4
print("a&b",a&b)

print(bin(4),bin(3),"=",bin(4&3))
print(4&3)

print(4 and 3)
print(str("Python") and str("Java"))
# print("Python" & "java")        #it give type error

print("---Example------")
#common element like the inteerssection
s1={10,20,30}
s2={30,40,50}
s3=s1&s2
print(s3,type(s3))

s3=s1.intersection(s2)
print(s3,type(s3))

#common element is put output
s1={1.2,2.3,4.5}
s2={2.3,4.5,5.6}
s3=s1&s2
print(s3,type(s3))