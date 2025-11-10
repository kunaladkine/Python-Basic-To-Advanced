#Bitwise XOR Operator ( ^ )
#Syntax : value1^value2

print(1^0)
print(0^1)
print(1^1)
print(0^0)

print("-----Example-----")
a=2
b=3
c=a^b
print(f"{a} and {b} : {c}")
print("------Addition------")
print(bin(a),"and",bin(b),":",bin(a^b))

print("------Example----")

a={1.2,3.4,4.5}
b={4.5,1.2,3.4}
c=a^b
#it will print empty set , all values are same no unique value
print(c)

print("------Example------")
a={1.1,3.4,4.5}
b={4.5,1.5,3.4}
c=a^b
#Here Print Because unique Value by According to Rule
print(c)