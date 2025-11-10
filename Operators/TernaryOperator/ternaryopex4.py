#Program for accepting Three Numerical Values and Find Biggest and Check for equality

a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
c=float(input("Enter Value of c:"))

res=a if b<=a>c else b if a<b>=c else c if a<=c>b else "Both Value are same"
print("Max({},{},{})={}".format(a,b,c,res))