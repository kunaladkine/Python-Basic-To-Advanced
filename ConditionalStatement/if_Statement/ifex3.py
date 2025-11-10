#write a python program which will accept a word and check palindrome or not.

value=input("Enter Any Word:")
if(value.lower()==value[::-1]):
    print("it is Palindrome")
if(value.lower()!=value[::-1]):
    print("It is not Palindrome.")
print("Program Execute Successfully..!")