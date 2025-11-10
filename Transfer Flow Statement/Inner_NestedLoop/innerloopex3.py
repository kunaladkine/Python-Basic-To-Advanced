#for loop in while loop
i=5
while(i>=1):    #outer loop
    print("_"*50)
    print("Outer loop - Value of i=",i)
    print("_"*50)
    for j in range(3,0,-1): #inner Loop
        print("\tInner Loop-Value of j=",j)
    else:
        i=i-1
        print("\tOut - Off Inner Loop")
        print("_"*50)
else:
    print("_"*50)