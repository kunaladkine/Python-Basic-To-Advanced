#Membership Operator
#In Operator

s="PYTHON"
print(s,type(s))
print('P' in s)
print('K' in s)
print('PYT' in s)
print('KVR' in s)
print('KVR' not in s)
print('PYT' not in s)

print("------Ex 2-------")
s="PYTHON"
print(s,type(s))
print("PTO" in s)
print('PTO' in s[::2])
print('NOH' in s)
print('NOH' in s[::-1])

print("----Ex 3-----")

lst=[10,"Rossum",45.67,2+3j]
print(lst,type(lst))
print('sum' not in lst[1])
print('sum' in lst[1])
# print(2+3j in lst[-1])

print("-----Ex 4-----")
d1={1:"python",2:"java",3:"dsa"}
print(d1,type(d1))
print('python' in d1)
print(10 in d1)
print(1 in d1)

print("-----ex5-----")
d1={1:"python",2:"java",3:"dsa"}
print('python' in d1.values())
print((1,'python' ) in d1.items())

print("------Ex6-----")
lst=[10,"RS",54,67,90]
print(lst,type(lst))
print(lst in lst)

print("-----Ex7-----")
lst=[10,"RS",[45,67,90]]
print(lst,type(lst))
print(lst[-1] in lst)

