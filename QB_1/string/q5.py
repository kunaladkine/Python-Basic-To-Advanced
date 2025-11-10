# Python program to split and join a string
s=input("Enter Any Sentence:")
res=s.split()
print("The Split String is : {}".format(res))
res2=" "
joinstr=res2.join(res)
print("The Join String is : {}".format(joinstr))