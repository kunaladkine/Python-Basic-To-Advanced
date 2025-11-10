#program for accepting a Word and Decide whether It is Vowel Word Or Not
#TernaryOpEx6.py
word=input("Enter Any Word:") # Mango
res="Vowel Word" if set("aeiouAEIOU").intersection(set(word)) else " Not Vowel Word "
print("{} is {}".format(word,res))