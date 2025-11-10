#program for accepting a Word and Decide whether It is Vowel Word Or Not

word=input("Enter Any World : ")
res="Vowel Word" if ("a" in word or "e" in word or
                     "i" in word or "o" in word or
                     "u" in word or "A" in word or
                     "E" in word or "I" in word or
                     "O" in word or "U" in word) else "Not Vowel Word"
print("{} is {}". format(word,res))