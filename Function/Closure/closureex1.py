#Program for showing the need of Closures
#ClosureEx1.py
def  PythonAuthor(sname): # Outer Function
	print("I am from Outer Function:{}".format(sname))
	def  welcome(pname): # Inner Function--closure
		print("Hi {}, {} is welcoming for Learning Python".format(pname,sname))
	return welcome

#Main Program
wc=PythonAuthor("GUIDO VAN ROSSUM")   # Outer Function Call
wc("Ritche") # Inner Function Call
wc("Travis")  # Inner Function Call
wc("Kinney")  # Inner Function Call