#programm for accepting a line of text and get its upper case and lower case by using decorators concept

def tolower(cc):
    def caseconvert():
        line,uc=cc()
        lc=line.lower()
        return line,uc,lc
    return caseconvert

def toupper(gl):
    def convertcase():
        line=gl()
        uc=line.upper()
        return line,uc
    return convertcase

@tolower
@toupper
def getline():
    return input("Enter Line of Text:")


#main program
line,uc,lc=getline()
print("given Line=",line)
print("Upper Case:",uc)
print("Lower Case=",lc)