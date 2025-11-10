#BitWise Or " | " Operator
print(1|0)
print(0|1)
print(0|0)
print(1|1)

print("------------Example 1----------")

a=4
b=3
c=a|b
print(bin(4),"and",bin(3), "=",bin(4+3))
print(f"{a} and {b} : {c}")

print("--------Example 2 -------")

a=10
b=10
c=a|b
print(bin(4),"and",bin(3), "=",bin(4+3))
print(f"{a} and {b} : {c}")

print("--------Example 3 -------")

a=15
b=3
print("a|b = ",a|b)

print("--------Example 4 -------")

a={10,20,30}
b={15,30,45}
c=a.union(b)
print(c,type(c))

print("-----OR---------")
c=a|b
print("In BitWise OR : ",c)

print(a or b)