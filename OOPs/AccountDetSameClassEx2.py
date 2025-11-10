class Account:
    def __init__(self):
        self.__acno=1234
        self.cname="Rossum"
        self.__bal=5.6
        self.__pin=4578
        self.bname="SBI"
    def __getaccdet(self):
        print("Account Number=", self.__acno)
        print("Account Holder Name=", self.cname)
        print("Account Balance=", self.__bal)
        print("Account Pin=", self.__pin)
        print("Account Branch Name=", self.bname)
    def dispaccdet(self):
        self.__getaccdet()

#Main Program
ac=Account()
#ac.__getaccdet() # Can't access from main program
ac.dispaccdet()
