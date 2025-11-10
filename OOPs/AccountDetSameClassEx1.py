class Accouunt:
    def __init__(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal=4.4
        self.__pin=3455
        self.bname="SBI"

    def dispaccdet(self):
        print("Account Number=", self.__acno)
        print("Account Holder Name=", self.cname)
        print("Account Balance=", self.__bal)
        print("Account Pin=", self.__pin)
        print("Account Branch Name=", self.bname)

#main program
ac=Accouunt()
ac.dispaccdet()
"""print("Account Number=",ac.acno)   Can't access from main program
print("Account Holder Name=",ac.cname)
print("Account Balance=",ac.bal)
print("Account Pin=",ac.pin)
print("Account Branch Name=",ac.bname)"""