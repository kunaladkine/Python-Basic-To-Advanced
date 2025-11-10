#program for cal div of Two Numebrs by handling all Possible Exceptions
#DivEx11.py
#This Program developed by KVR on 28/8/2025 handled Two Exceptions
#After 4 Years28/8/2029, This Code comes for Project Maintenance----Modification-New Programmer Called Ram
try:
	print("Program Execution  Started")
	s1=input("\tEnter First value:")
	s2=input("\tEnter Second value:")
	#Convert str data into int type
	a=int(s1)  # Exception generated stmt------ValueError
	b=int(s2) # Exception generated stmt------ValueError
	#Cal Div
	c=a/b  # Exception generated stmt------ZeroDivisionError
	#New Statement
	s="PYTHON"
	print(s[10])
except (ZeroDivisionError,ValueError,IndexError):
	print("\tDON'T ENTER ZERO FOR DEN...")
	print("\tDON'T ENTER ALNUMS,STRS AND SYMBOLS...")
	print("\tPLZ CHECK THE INDEX")
except BaseException: # generic except block
	print("\tOooooops, Some Thing went wrong!!!")
else:
	print("----------------else----------------")
	print("\tValue of a={}".format(a))
	print("\tValue of b={}".format(b))
	print("\tDiv={}".format(c))
finally:
		print("Program Execution  Completed")
