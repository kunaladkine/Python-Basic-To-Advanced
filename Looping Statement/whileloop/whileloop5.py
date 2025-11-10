#program for accepting a word/line and display each and every letter
#whileloop5.py

line=input("Enter a Line of Text :")
print("By using while loop--Forward Direction +ve Indices.")
i=0
while(i<len(line)):
    print("\t{}".format(line[i]))
    i=i+1
print("_"*50)
print("By using While loop--Forward Direction -ve Indices.")
i=-len(line)
while(i<=-1):
    print("\t{}".format(line[i]))
    i=i+1
print("_"*50)
print("by using while loop -- Backward Direction +ve indices.")
i=len(line)-1
while(i>=0):
    print("\t{}".format(line[i]))
    i=i-1
print("_"*50)
print("By using while loop--Backward Direction -ve Indices.")
i=-1
while(i>=(-len(line))):
    print("\t{}".format(line[i]))
    i=i-1
print("_"*50)