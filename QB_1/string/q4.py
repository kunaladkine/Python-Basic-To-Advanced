# Python program to accept the strings which contains all vowels

s=input("Enter Any Word :")
res="Not Vowel Word" if set("aieouAEIOU").isdisjoint(set(s)) else "Vowel Word"
print("{} is {}".format(s,res))

res="vowel word" if set("aeiouAEIOU").intersection(set(s)) else "Not Vowel Word"
print("{} is {}".format(s,res))