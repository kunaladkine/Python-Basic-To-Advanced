a=[]
b=input("Enter Your Name: ")
c=int(input("Enter Your Age : "))
d=input("Enter Your Course :  ")
a.append(b)
a.append(c)
a.append(d)
print(a,type(a))

update_name1=a.insert(0,(input("Enter Your New Name : ")))
update_name2=a.pop(1)
update_course=a.insert(2,(input("Enter Course : ")))
update_course1=a.pop(-1)

print(a)

