s="MISSISSIPPI"
print("By ussing while loop")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("i am from else part of while loop")
print("_"*50)
ctr=0
i=0
while(i<len(s)):
    if(s[i]=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
    print(s[i],end="")
    i=i+1
else:
    print("I am from else part of while loop")
print()
print("_"*50)