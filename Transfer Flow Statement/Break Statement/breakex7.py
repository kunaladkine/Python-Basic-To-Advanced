#program for accepting a word and decide whetheer it Vowel word or not

word=input("Enteer any word :")
res="NOT VOWEL"
for ch in word:
    if(ch.lower() in list("aeiou")):
        res="VOWEL WORD"
        break
print("{} is {}".format(word,res))