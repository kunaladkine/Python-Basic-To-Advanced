#Check if a person is eligible to vote using the ternary operator.

per_age=int(input("Enter Age : "))
res="Can Vote " if per_age>=18 else "not Eligible"
print("You are {}".format(res))