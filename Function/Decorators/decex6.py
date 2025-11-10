#programm for accepting a line of text and get its upper case and lower case by using decorators concept

def toupper(gl):
    def convertcase():
        line=gl()
        uc=line.upper()
        return line,uc
    return convertcase

def getline():
    return input("Enter Line of Text:")

#main program
uc=toupper(getline)
line,uppercasse=uc()
print("given line=",line)
print("Upper Case:",uppercasse)