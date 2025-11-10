#Program for accepting a Line of Text and Get Its Upper case and Lower Case by using Decorators Concept
#DecEx8.py
def tolower(cc):
	def caseconvert():
		line,uc=cc()
		lc=""
		for ch in line:
			if ord(ch) in range(65,91):
				lc=lc+chr(ord(ch)+32)
			else:
				lc=lc+ch
		return line,uc,lc
	return caseconvert

def toupper(gl):
	def convertcase():
		line=gl()
		uc=""
		for ch in line:
			if ord(ch) in range(97,123):
				uc=uc+chr(ord(ch)-32)
			else:
				uc=uc+ch
		return line,uc
	return convertcase

@tolower
@toupper
def getline():  # tolower(toupper(getline)))
	return input("Enter Line of Text:")

#Main Program
line,uc,lc=getline()
print("Given Line=",line)
print("Upper Case=",uc)
print("Lower Case=",lc)