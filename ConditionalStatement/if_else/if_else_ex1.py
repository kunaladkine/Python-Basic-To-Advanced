#program for reading a word and decide wheter it is palindrrome or not by using if else sstatement.

word=input("Enter Any Word:")
if(word.lower()==word[::-1]):
    print("{} is Palindrome.".format(word))
else:
    print("{} is not Palindrome.".format(word))
print("Program Execution Completed..!")