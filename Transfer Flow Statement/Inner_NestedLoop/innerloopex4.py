#While Loop In For Loop
for i in range(1,6):
    print("_"*50)
    print("Outer Loop-Value of i=",i)
    print("_"*50)
    j=3
    while(j>=1):
        print("\tInner Loop-Value of j=",j)
        j=j-1
    else:
        print("\tOut -off Inner Loop")
        print("_"*50)
else:
    print("_"*50)