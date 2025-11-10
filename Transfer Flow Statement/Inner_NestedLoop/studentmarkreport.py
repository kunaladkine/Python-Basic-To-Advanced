#program for generating mrks report

#validation code for student name
while(True):
    sno=int(input("Enter Student Number:"))
    if sno in range(100,201):
        break
    print("\t{} is invalid Student Number-- try again".format(sno))

#validation code for student Name
while(True):
    name=input("Enter Ur Name:")
    if(len(name)==0):
        print("\t Must Ente Ur Name -try again:")
    elif(name.isspace()):
        print("\t Don't Enter space of Ur Name --try again:")
    else:
        res=True
        words=name.split()
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            break
        print("\t{} is invalid Name-try again".format(name))

#validation code for C-Lang Marks
while(True):
    cm=int(input("enter C-lang Mrks:"))
    if(0<=cm<=100):
        break
    print("\t{} is invalid marks -try again".format(cm))

#validation for for cpp langmarks
while(True):
    cppm=int(input("Enter CPP-Lang Marks:"))
    if(0<=cppm<=100):
        break
    print("\t{} is Invalid Marks -try again".format(cppm))

#validation for pym marks

while(True):
    pym=int(input("Enter Python Lang Marks:"))
    if(0<=pym<=100):
        break
    print("\t {} Is Invaid marks - try again".format(pym))

#Calculate total markss \

totalmarks=cm+cppm+pym

#calculate percentage of mrks
percent=(totalmarks/300)*100

if(cm<40) or (cppm<40) or (pym<40):
    grade="Fail"
else:
    if(75<=percent<=100):
        grade="Distinction"
    elif(60<=percent<75):
        grade="First"
    elif(50<=percent<60):
        grade="Second"
    elif(40<=percent<50):
        grade="Third"
print("_"*50)
print("\tStudent Marks Report")
print("_"*50)
print("\tStudent Number:{}".format(sno))
print("\tStuednt Name: {}".format(name))
print("\tStudent Marks In C Lang: {}".format(cm))
print("\tStudent Marks in CPP Lang: {}".format(cppm))
print("\tStudent Marks in Python Lang: {}".format(pym))
print("\tStudent Total Marks :{}".format(totalmarks))
print("\tStudent Percentage of Marks :{}".format(percent))
print("\tStudent Grade :{}".format(grade))
print("_"*50)