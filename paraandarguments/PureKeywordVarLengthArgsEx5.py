#Program for Demonstrating the Need of   Keyword Variable Length Arguments
#This program will  execute as It is
#PureKeywordVarLengthArgsEx5.py
def  findtotalmarks(rno,sname,cls,*intmarks,city="HYD",**submarks):
	print("="*50)
	print("\tStudent Number={}".format(rno))
	print("\tStudent Name={}".format(sname))
	print("\tStudent Class={}".format(cls))
	print("\tStudent Living City={}".format(city))
	print("-"*50)
	print("List of Var Length Vals")
	for val in intmarks:
		print("\t{}".format(val))
	print("-"*50)
	totmarks=0
	print("\tSubject\t\tMarks")
	print("-"*50)
	for subject in submarks:
		print("\t{}\t\t{}".format(subject,submarks.get(subject)))
		totmarks+=submarks.get(subject)
	print("-"*50)
	print("\tTOTAL MARKS={}".format(totmarks))
	print("-"*50)

#main Program
findtotalmarks(10,"RS","X",1.2,2.3,4.5,5.5,Telugu=80,Hindi=90,English=90,Maths=99,Science=90,Social=89)
findtotalmarks(20,"DR","XII",11.2,22.2,10.2,9.2,1.2,Sanskrit=99,English=95,Maths_1A=75,Physics=60,Chemstry=59)
findtotalmarks(30,"RT","B.Tech(CSE)",11,22,33,OS=40,DBMS=50,NW=45)
findtotalmarks(40,"MC","Research",5,6,7,city="NL")
findtotalmarks(50,"DT","Politics",Eco=20,Pol=23,Civ=25,city="USA")
findtotalmarks(60,"PT","Eco-Politics",22,33,11,city="RSA",Come=20,Pol=23,comp=25)