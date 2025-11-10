#program for call sum of n natural numbers, squares and cubes of n natural nums
n=int(input("Enteer how many natural nums sum want:"))
if(n<=0):
    print("Invaid Input")
else:
    s,ss,sc=0,0,0
    print("_"*50)
    print("Nat Nums\tSquares\t\tCubes")
    print("_"*50)
    for i in range(1,n+1):
        print("\t{}\t\t\t{}\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        sc=sc+i**3
    else:
        print("_"*50)
        print("\t{}\t\t\t{}\t\t\t{}".format(s,ss,sc))
        print("_"*50)