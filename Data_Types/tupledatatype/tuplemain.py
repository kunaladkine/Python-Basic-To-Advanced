#to stor data or values in tuple we must write the values within braces () and values separated by comma.

# Syntax: varname=(val1,val2,val3,....,val-n)

#Empty Tuple
#Syntax 1 : varname=()
#Syntax 2 : varname=tuple()

#Non-Empty Tuple
#Syntax 1 : varname=(vale1,val2,...,val-n)
#syntax 2 : varname=val1,val2,val3,...val-n
#syntax 3 : varname=tuple(Iterable-object)
#syntax 4 : varname=tuple([Iterable-object])
#syntax 5 : varname=tuple([Non-Iterable-Object])
#syntax 6 : varname=tuple((non-Iterable-object,))    , comma is used there

t1=(10,20,30,40,50)
print(t1,type(t1))

t2=(10,100,20.33,"rahul",2+3j,True)
print(t2,type(t2))

# using indexing
print(t2[0])
print(t2[1])
print(t2[-1])

# using slicing

print(t2[1:3])
print(t2[::-1])
print(t2[::2])


print(len(t2))

# --------------------------------------------- #

s="PYTHON"
print(s,type(s))
t=tuple(s)
print((t,type(t)))
t=tuple([s])             #strig to tuple

print(t,type(t))

# -----------------------------#

a=10
print((a,type(a)))
# t=tuple(a)
# print((t,type(t)))             it gives the error because  int is  not  iterable
t=tuple([a])
print(t)
t=tuple((a,))         #to convert the int into tuple use value and comma ,
print(t)

