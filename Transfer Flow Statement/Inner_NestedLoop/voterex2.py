#program for accpeting age of citizen and decide whether the citizen is eligible to vote or not

while(True):
    age=int(input("Enter Age of Citizen:"))
    if(age>=18) and (age<=100):
        print("\t {} years Citizen is Eligible to Vote :".format(age))
        break
        print("\t {} Years citizen is Not Eligible to vote --try again:".format(age))