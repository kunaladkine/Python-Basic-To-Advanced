#Accept total bill and number of friends. Print how much each friend pays and leftover paise.

bill=float(input("Enter Total Bill Amount:"))
frd=int(input("Enter Toal No of Firends: "))

#Input of Bill and No of friends
print("Total Bill Amount is : ₹{} and Friends To Be Distributed = {}".format(bill,frd))

#Eachh Pays
eachpay=bill//frd

#reamin pay
remainpay=bill%frd

print("Each Pay = {}".format(eachpay))

print("Remaining = {}".format(remainpay))