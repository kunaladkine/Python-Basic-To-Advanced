#Program for showing the Dispatching the currency in terms of number of Notes.
#arithmeticex3.py

wamt=int(input("Enter ur withdraw Amount : "))
#How many Notes 500 to be given

n500=wamt//500
wamt=wamt%500

#how many notes 300 to be given

n200=wamt//200
wamt=wamt%200

#how many notes 100 to be given

n100=wamt//100
wamt=wamt%100

print("Number of 500={}".format(n500))
print("Number of 200={}".format(n200))
print("Number of 100={}".format(n100))