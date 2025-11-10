#program for demonstrating the need of data Encapsulation
#Account1.py<----- File Name and Module name

class Account:
    def __init__(self):
        self.__acno=123
        self.cname="Rossum"
        self.__bal=4.4
        self.__pin=4563
        self.bname="SBI"

