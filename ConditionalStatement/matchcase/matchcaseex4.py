import sys
s="""------------------------------
Temperature Conversion Calculator
------------------------------------
            1. C to F
            2. C to K
            3. F to C
            4. F to K
            5. K to F
            6. K to C
            7. Exit
-----------------------------------
"""
print(s)
ch=input("Input Ur Choice :")
match(ch):
    case "1":
        c=float(input("Enter Value C="))
        f=c*(9/5)+32
        print("\tCelsius to Fahrenheit : {}".format(f))
    case "2":
        c=float(input("Enter Value of C:"))
        k=c+273.15
        print("\tCelsius to Kelvin : {}".format(k))
    case "3":
        f=float(input("Enter Fahrenheit Value :"))
        c=(f-32)*(5/9)
        print("\tFahrenheit to Celcius : {}".format(c))
    case "4":
        f = float(input("Enter Fahrenheit Value :"))
        k=(f-32)*(5/9)+23.15
        print("\tFahrenheit to Kelvin : {}".format(k))
    case "5":
        k=float(input("Enter Kelvin Value :"))
        f=(k-273.15)(9/5)+32
        print("\tkelvin To Fahrenheit : ".format(f))
    case "6":
        k=float(input("Ente Kelvin Value :"))
        c=k-273.15
        print("\tKelvin To Celcius : {}".format(c))
    case "7":
        sys.exit()
    case _:
        print("UR Value is Wrong. Try Again . ")