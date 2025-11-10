#write a python program to get words and check palindrome or not
print("Enter List Of Words Separated by space :")
words=[word for word  in input().split()]
print("Given Word is :",words)
pword=list(filter(lambda word: word==word[::-1],words))
print("Palindrome Word ;",pword)
