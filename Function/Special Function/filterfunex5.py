#program for reading llist of words and
#filter those words whose first and lastletters are same

print("Enter List of Values Separated By Space :")
lst=[val for val in input().split()]
print("List of Words ")
print(lst)
flwords=list(filter(lambda word: word[0]==word[-1] and word!=word[::-1],lst))
print("List of Words Whose First and Last Letters are Same ;")
print(flwords)