#program for demonstrating continue statement
from enum import CONTINUOUS

s="PYTHON"
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("_"*50)
i=0
while(i<len(s)):
    if(s[i]=="T") or (s[i]=="O"):
        i=i+1
        continue
    print("{}".format(s[i],end=""))
    i=i+1
else:
    print("_"*50)
