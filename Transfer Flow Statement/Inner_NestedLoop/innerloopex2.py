#While Loop In while Loop

i=1
while(i<=5):    #outer loop
    print("_"*50)
    print("Outer Loop Value of i=",i)
    print("_"*50)
    j=1
    while(j<=3):
        print("\tInner Loop Value of j=",j)
        j=j+1
    else:
        i=i+1
        print("\tOut-off Inner Loop")
        print("_"*50)
else:
    print("_"*50)