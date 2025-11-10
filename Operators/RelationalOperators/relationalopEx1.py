#while we are comparing string values then we must consider UNICODE value of every letter of string data
print("RAT">"CAT")
print("ATR">"ATC")
print("aTR">"ATC")
print("ATR">"aTC")
print(" ">"$")
print(ord(" "))
print(ord("4"))

print("_"*60)

#to find the Unicode code value of any symbol OR Alphabet, we use ord()
#Syntax = ord("Symbl/alphabet")

#to find symbol or alphabet of any unicode code value, we use chr()
#syntax : Syntax: chr(unicode code value )

print(chr(32))
print(chr(36))
print(chr(65))
print(chr(97))