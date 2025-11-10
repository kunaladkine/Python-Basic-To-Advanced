#program for validating the name of persson/product/place

name=input("Enter Ur Name:")
if(len(name)==0):
    print("\t U Must enter ur name")
elif(name.isspace()):
    print("\t Ur name should not space")
else:
    words=name.split()
    res="Valid"
    for word in words:
        if(not word.isalpha()):
            res="Invalid"
            break
    print("{} is {}".format(name,res))