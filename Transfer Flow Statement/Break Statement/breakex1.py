#program for deomstratin the need of break key word
s="PYTHON"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
print("_"*50)
for ch in s:
    if(ch=="O"):
        break
    print(ch,end="")
else:
    print("I am from else part of for loop")
print()
print("_"*50)