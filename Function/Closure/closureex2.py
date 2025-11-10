#Program for showing the need of Closures
#ClosureEx2.py
def  PythonAuthor(sname): # Outer Function
	print("I am from Outer Function:{}".format(sname))
	def  welcome(pname): # Inner Function--closure
		print("Hi {}, {} is welcoming for Learning Python".format(pname,sname))
	welcome("Ritche") # Inner Function Call
	welcome("Travis")  # Inner Function Call
	welcome("Kinney")  # Inner Function Call

#Main Program
PythonAuthor("GUIDO VAN ROSSUM")   # Outer Function Call
