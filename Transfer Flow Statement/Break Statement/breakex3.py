#program for demonstratin the need of break key word
s="MISSISSIPPI"
print("By Using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
ctr=0
for ch in s:
    if(ch=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
    print(ch,end="")
else:
    print("I am from else part of for loop")
print()
print("_"*50)
