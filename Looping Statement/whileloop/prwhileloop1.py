# Write a Python program that accepts a positive integer n and prints all even numbers from 1 to n, along with the count and sum of those even numbers.

n=int(input("Enter Any Integer Number :"))
if(n<=0):
    print("{} invalid number".format(n))
else:
    print("_"*50)
    print("Integer Number : {}".format(n))
    print("_"*50)
    i=0
    while(i<n):
        if(i%2!=0):
            print("\t{}".format(i))
        i+=1
    else:
        i=i+1
        print("_"*50)
