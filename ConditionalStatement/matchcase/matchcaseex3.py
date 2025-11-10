s="""--------------------------
Base Conversion Calculator
-------------------------------
I. Dec To Binary
    Dec To Octal
    Dec To hexa
II. Binary to Dec
    Binary to Oct
    Binary to hexa
III. Octal to Dec
    Octal to Binary
    Octal to Hexa
Iv. Hexa to Dec
    Hexa to Binary
    Hexa to Octal
--------------------------------"""
print(s)
ch=input("Enter the Choice for Base Conversions:")
match(ch):
    case "I":
        dv=int(input("Enter The Decimal Number System Value:"))
        print("bin({})={}".format(dv,bin(dv)))
        print("oct({})={}".format(dv,oct(dv)))
        print("hex{{})={}".format(dv,hex(dv)))
    case "II":
        bv=input("Enter the Binary Number System Value preceded 0b or 0B:")
        dv=int(bv,2)
        print("Dec({})={}".format(bv,dv))
        print("oct({})={}".format(bv,oct(dv)))
        print("hex({})={}".format(bv,hex(dv)))
    case "III":
        ov=input("Enter the Octal Number System Value precede 0o or 0O :")
        dv=int(ov,8)
        print("Dec({})={}".format(ov,dv))
        print("Bin({}={}".format(ov,bin(dv)))
        print("Hex({})={}".format(ov,hex(dv)))
    case "IV":
        hv=input("Enter the Hexa Decimal Number System Value preceded 0x or 0X :")
        dv=int(hv,16)
        print("Dec({})={}".format(hv,dv))
        print("Bin({})={}".format(hv,bin(dv)))
        print("Oct({})={}".format(hv,oct(dv)))
    case "V": pass
    case _:
        print("Ur Selection of Operation wrong - try again.")