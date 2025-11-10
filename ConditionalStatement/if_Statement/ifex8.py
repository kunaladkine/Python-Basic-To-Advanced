a=float(input("Enter Value : "))
b=float(input("Enter Value :"))
c=float(input("Enter Value :"))

if(b<=a>c):
    print(f"{a},{b}and {c} is {a} Big")
if(a<=b>c):
    print(f"{a},{b}and {c} is {b} Big")
if(a<=c>b):
    print(f"{a},{b}and {c} is {c} Big")
if(a==b==c):
    print("All Values are Equal.")
