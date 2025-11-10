#Syntax : setobj.remove(Value)
#thiss function is used for removing the specified value form set object.
#if the specified value does not exist in set object then we get keyerror.

s1={10,"Travis",34.44,True, 2+3j}
print((s1),type(s1))
s1.remove(10)
print(s1)
print(s1.remove(34.44))     #remove the value what we given in remove fun element
s1.remove(100000)       #it will print KeyError:100000
set(s1.remove(10000))       #it also print the KeyError:10000

