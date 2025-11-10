#programm for demonstrating continue statement using while loop
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("_"*50)
i=0
while(i<len(s)):
    if(s[i]=="H"):
        I=i+1
        continue
    print("{}".format(s[i],end=""))
    i=i+1
else:
    print("*"*50)