# Python program to find uncommon words from two Strings

# s="python"
# r="kunal"

s=input("Enter First String :")
r=input("Enter Second String :")
res=set(s).symmetric_difference(set(r))
print("The Uncommon word is :{}".format(res))