"""line=input("Enter Line of Text :")
digs=list(filter(lambda ch: ch.isdigit(),line))
ssym=list(filter(lambda ch: ch.isalpha(),line))
print("Digits Found")
print("Special Symbol :")
print(",".join(digs))
print(",".join(ssym))"""

"""l=[1,2,3,4,5,6,7,8,9]
s=list(map(lambda x:x*x,l))
print(s)"""

"""def square(x):
    return x*x
l=[1,2,3,4,5,6,7,8,9]
d=list(map(square,l))
print(d)"""

"""l=[1,2,3,4,5,6,7,8,9,10,11,12,13,134,222,3333,4444]
s=list(filter(lambda x:x%2==0,l))
print(s)"""

"""def even(x):
    return x%2==0
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,1 2 3134,222,3333,4444]
s=list(filter(even,l))
print(s)"""

"""emails = ["a@b.com", "bad@.com","a.com", "@oops.com", "ok@mail.org"]
for i in emails:
    if '@'in i and '.' in i.split("@")[-1]:
        print(i)"""

# l=list(map(int ,input("enter values seperted by comma").split(',')))
# print(l)
# l=[int(i) for i in input("enter values seperTED BY spaces:").split(" ")]
# print(l)
names=["kunal","ramu","naresh"]
l=list(map(str.upper,names))
print(l)