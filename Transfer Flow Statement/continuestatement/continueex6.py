#program for accepting a line of text and cconvert it into lower and upper casse .
#whitout using lower() and upper()

line=input("Enter a line of Text:")
print("Given Line:")
print("\t{}".format(line))
print("_"*50)
lc=""
uc=""
for ch in line:
    if ord(ch) in range(65,91):
        lc=lc+chr(ord(ch)+32)
    else:
        lc=lc+ch
for ch in line:
    if ord(ch) in range(97,123):
        uc=uc+chr(ord(ch)-32)
    else:
        uc=uc+ch
print("_"*50)
print("Lover Case Text:",lc)
print("Upper Case Text:",uc)
print("_"*50)