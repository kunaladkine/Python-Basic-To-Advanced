#1.Capitalize() - only first letter will be capital.

print("----------capitalize()---------")
s="python"
a="python is oop lang"
b="Python Is AN OOp Lang"
c="python is an oop.lang"
s=s.capitalize()        #assigning value not possible in str immputable object
print(s)
print(s.capitalize())       #make first letter capital
print(a.capitalize())
print(b.capitalize())

#2. title()  - make the every word becoming capital.
print("----------title()---------")
print(s.title())
print(a.title())
print(b.title())
print(c.title())

#3. count() - to count the how manytime letter will come in str.
print("----------count()---------")
d="RADAR"
print(d.count("R"))
print(d.count("A"))
print(d.count("K"))     #will print 0 no letter has available
print(d.count("RA"))
print(d.count("DAR"))

#4. swapcase() - to change capital to small and small to capital
print("----------{IMP - swapcase() }---------")
r="PyThOn"
print(r.swapcase())         #swaping the case
r="PYTHON"
print(r.swapcase())
r="python"
print(r.swapcase())

#5. upper() - to capitalize each word into Capitalcase
print("----------upper()---------")

print(s.upper())
print(a.upper())
w="Python3.12"
#for number and symbol no uppercase is consun.
print(w.upper())

#6. lower() - to change the word into lowercase
print("----------lower()---------")
print(a.lower())
print(s.lower())
print(b.lower())
print(r.lower())

#7. isupper() - to check the upper case or not
print("----------isupper()---------")
x="PYTHON"
print(x.isupper())
y="python"
print(y.isupper())
g="cat34@"
print(g.isupper())


#8. islower() - to check the lower case or not
print("----------islower()---------")

print(x.islower())
print(y.islower())
print(g.islower())

#9. isdigit()
print("----------isdigit()---------")

#10 isalpha()
print("----------isalpha()---------")

#11 isalnum()
print("----------isalnum()---------")

#12 rstrip() - removes right side unwanted space.
print("----------rstrip()---------")

#13. lstrip() - removes left side unwanted space.
print("----------lstrip()---------")

#14. strip() - removes left and right side space.
print("----------strip()---------")

#15. split()
print("----------split()---------")

#16.
print("----------isalnum()---------")
