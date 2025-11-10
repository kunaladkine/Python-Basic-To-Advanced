#program for demonstrating  the need of local and global variables

def learnAI():
    sub1="AI"       #here sub1 is called local variable
    print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub1,lang))
def learnML():
    sub2="ML"
    print("\tTo Implement '{}' Based Applications, we use '{}' Lang.".format(sub2,lang))

#main program
lang="Python"       #here 'lang' is called global variable
learnAI()
learnML()