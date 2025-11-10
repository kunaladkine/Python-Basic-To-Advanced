#program for cal div of Two Numebrs by handling all Possible Exceptions
#DivEx7.py
try:
	print("Program Execution  Started")
	s1=input("\tEnter First value:")
	s2=input("\tEnter Second value:")
	#Convert str data into int type
	a=int(s1)  # Exception generated stmt------ValueError
	b=int(s2) # Exception generated stmt------ValueError
	#Cal Div
	c=a/b  # Exception generated stmt------ZeroDivisionError
except Exception : # generaic except block
	print("Oooooops. Some thing went wrong!!")
else:
	print("----------------else----------------")
	print("\tValue of a={}".format(a))
	print("\tValue of b={}".format(b))
	print("\tDiv={}".format(c))
finally:
		print("Program Execution  Completed")