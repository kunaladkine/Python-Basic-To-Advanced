#program for accepting a Word and Decide whether It is Vowel Word Or Not
word=input("Enter any word : ")
res="Not Vowel Word" if set("aeiouAEIOU").isdisjoint(set(word)) else "Vowel Word"
print("{} is {}".format(word,res))