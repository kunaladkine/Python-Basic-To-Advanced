#we know that on the object of tuple we can perform both indexing and slicing operations.
#along with these operations, we can also perform other operations by using the following.

#1. index()
t1=(10,"RS",45.33)
print(t1,type(t1))

print(t1.index(10))
print(t1.index("RS"))

# -------------------------

#2. count()
t2=(10,20,30,10,20,10,10,50,60)
print(t2.count(10))
print(t2.count(30))

# -----------------------------
y=tuple(sorted(t2,reverse=True))
print(y)
y=tuple(sorted(t2)[::-1])
print(y)

# -----------------------------

t3=(10,-4,12,34,16,-5,0,15)
print(t3,type(t3))

l1=list(t3)
print(l1,type(l1))

l1.sort()
print(l1)
t4=tuple(l1)
print(t4,type(t4))
t5=t4[::-1]
print(t5)

# ----------------------------------