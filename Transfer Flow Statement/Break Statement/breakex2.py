#program for demonstraint the need of break key word
s="PYTHON"
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of while loop")
print("_"*50)
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print(s[i],end="")
    i=i+1
else:
    print("I am from else part of while loop")
print()
print("_"*50)