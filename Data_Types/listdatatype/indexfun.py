#syntax : Listobj.index(value)
#this function is used for obtaining first occurence index of specified value from list object
#if the specified value does not exist then we get valueerror.

s="MISSISSIPPI"
print(s)
lst=list(s)
print(lst)
print(len(lst))

# to find the M index position
print(lst.index("M"))

print(lst.index("I")) #it will take only single value and first index show of letter

print(lst.index("K"))  # k is not in the list so it will give ValueError:

