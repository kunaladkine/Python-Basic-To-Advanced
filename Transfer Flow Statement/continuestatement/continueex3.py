#program for demonstrating continue statement
s="PYTHON"
print("by using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("_"*50)
for ch in s:
    if ch in["T","O"]:
        continue
    print("{}".format(ch),end="")
else:
    print("_"*50)




