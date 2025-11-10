#For Loop In for loop

for i in range(1,4):
    print("_"*50)
    print("Outer Loop Value of i=",i)
    print("_"*50)
    for j in range(1,4):
        print("\tInner Loop- value of j=",j)
    else:
        print("\tOut-off Inner Loop")
        print("-"*50)
else:
    print("_"*50)