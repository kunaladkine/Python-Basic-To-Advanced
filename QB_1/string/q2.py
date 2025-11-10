# Python program to check if a string is palindrome or not
s=input("Enter Any Word:")
if(s==s[::-1]):
    print("String Is palindrome")
else:
    print("Not Palindrome...!")