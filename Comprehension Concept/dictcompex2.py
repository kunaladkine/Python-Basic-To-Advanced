#dictcompex2s.py
n=int(input("Enter the Number of Values :"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        value=int(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("List of Random Values ")
        print(lst)
#cal square for every value of lst
d={val:val**2 for val in lst}
print("_"*50)
print("\tNumber\t\tSquare")
print("_"*50)
for k,v in d.items():
    print("\t{}\t\t\t{}".format(k,v))
print("_"*50)