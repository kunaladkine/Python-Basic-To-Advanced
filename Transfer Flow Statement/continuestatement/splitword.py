#program for accepting a line of text an ssplit the words without using split()
line=input("Enter a line of text:")
wordslist=[]
let=[]
for ch in line:
    if(ord(ch)!=32):
        let.append(ch)
    else:
        wordslist.append("".join((let)))
        let=[]
else:
    print(wordslist)