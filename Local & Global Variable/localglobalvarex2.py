#Program for Demonstrating the need of Local and Global Variables

lang="Python"       #here Lang is called Global Variable
def learnAI():
    sub1="AI"       #here sub1 is called local variable
    print("\tTo Implement '{}' Based Applications, we use '{}' Lang".format(sub1,lang))
def learnML():
    sub2="ML"
    print("\tTo Implement '{}' Based Applications, we use '{}' Lang.".format(sub2,lang))

#main program
learnAI()
learnML()