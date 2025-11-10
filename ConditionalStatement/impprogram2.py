#program for accepting a digit and display its name.
dobj={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
digit=int(input("Enter Any Digit:"))
print("{} is {} ".format(digit,dobj.get(digit) if dobj.get(digit)!=None else "+ve Number" if digit>0 else "-Ve Number" if digit<0 and digit not in range(-1,-10,-1) else "-Ve Number"
))