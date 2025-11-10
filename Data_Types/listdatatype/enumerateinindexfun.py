#the enumerate() must be applicable on iterable object only but not Non-Iterable objects.

#Syntax : for index,val in enumerate(Iterable-Object):
          #      print(index,"--->",val)

# ex1
s="MISSISSIPPI"
print(s)
lst=list(s)         #str convert to list
print(lst)

for x in enumerate(lst):            #it will print all index value of lit
    print(x)

for index,value in enumerate(lst):
    print(index,"-->",value)

# it will print only s and its index 
for index,value in enumerate(lst):
    if(value=="S"):
        print(index,"-->",value)