#programm for accepting a line of text and find length of each word

line=input("Enter a Line of Text:")
words=line.split()
d={}
for word in words:
    d[word]=len(word)
else:
    for word,length in d.items():
        print("\t{}-->{}".format(word,length))
print("_"*50)
lst=[]
for word in words:
    lst.append([word,len(word)])
else:
    for data in lst:
        print("\t{}--{}".format(data[0],data[1]))
print("_"*50)