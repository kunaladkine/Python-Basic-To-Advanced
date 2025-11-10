#program for demonstrating continue statement
s="PYTHON"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("_"*50)
for ch in s:
    if(ch=="H"):
        continue
    print("{}".format(ch),end="")
else:
    print()
    print("_"*50)