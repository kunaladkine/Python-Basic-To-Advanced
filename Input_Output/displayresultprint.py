#To Display the Result of Python Program on Console, we use a Pre-Defiend function called print().
#the print() can be used in 7 ways .

#Syntax 1 : print(val) or print(val1,val2,...,val-n)
#this function is used for displaying either single value or multiple values.

a=10
print(a)        #single value
a=10
b=20
print(a,b)      #multiple value
print("_"*50)
#-----------------------
#Syntax 2 : print(msg1) or print(msg1,msg2,...,msg-n) or print(msg1+msg2,...+msg-n)
print("Hello Python World")
print("Hellow","Python","World")
print("Hello"+"Python"+"World")
print("Hello"+" "+"Python"+' '+"World")
print(str("Hello")+str("Python")+str("World"))
print("_"*50)
#-----------------------
#Syntax 3 : print(message cum value) or print(value cum message)
a=10
print("Val of a=",a)
print(a,"Val of a")
print("val of a="+str(a))
print(str(a)+"Val of a")

a=10
b=20
c=a+b
print("Sum=",c)
print("Sum="+str(c))
print((c,"is the sum"))
print(str(c)+"is the sum")
print("sum of",a,"and",b,"=",c)
print("sum(",a,",",b,")=",c)
print("_"*50)
#---------------------
#Syntax 4 : print(message cum with format()) or print(value cum message with format())
a=10
print("val of a={}".format(a))
print("{} is the value".format(a))
b=20
c=a+b
print("sum of {} and {} is ={}".format(a,b,c))
print("sum({},{})={}".format(a,b,c))
print("_"*50)

#------------------------------------
#Syntax 5 : print(f"{val1},{val2},...,{val-n})
a=10
print(f"val of a={a}")
print(f"{a} is the val of a")
b=20
c=a+b
print(f"sum of {a} and {b} is {c}")
print(f"Sum({a},{b},{c})")
print("_"*50)
#------------------
#Syntax 6 : print(message cum value with format specifier) or print(value cum message with format specifier
# %d reperesents integer data
# %f represents flat data
# %s represents str data

a=10
print("val of a=%d" %a)
print("%d is the value of a" %a)
c=a+b
print("Sum of %d and %d is %d" %(a,b,c))
print("Sum(%d,%d=%d)" %(a,b,c))

a=1.2
print("a value is %f" %a)
print("%f is the value" %a)
print("value is %0.2f" %a)

a=12
print("val of a=%f" %a)
print("val of a=%0.3f" %a)

a=5.2356712
print("val of a=%f" %a)
print("val of a=%0.2f" %a)
print("val of a=%0.8f" %a)

lst=[10,"RS",34.33,2+3j]
print("content of lst=",lst)
print("Content of lst={}".format(lst))
print(f"Content of {lst}")
print("Content of lst=%s" %str(lst))
print("_"*50)

#---------------------------
#Syntax = print(val, end="delimeter")
#this syntax display the values in same line separated by 'delimeter'
for val in range(10,22,2):
    print(val,end=" ")
print("Single Line Print")
for val in range(10,22,1):
    print(val,end="-")