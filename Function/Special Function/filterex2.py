#find the negative and positive value using the anonymous function (lambda) function
positive=lambda val:True if val>0 else False
negative=lambda val:True if val<0 else False

# val=[10,20,30,-5,-99,-45,-97,11]
print("Enter List of Values With Separated By Comma :")
val=[float(val) for val in input().split()]
pvalue=list(filter(positive,val))
nvalue=tuple(filter(negative,val))

print("Postivie Value :",pvalue)
print("Negative Value :",nvalue)