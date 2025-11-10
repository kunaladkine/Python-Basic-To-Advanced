#program for demonstrating the need of variable length
#this program will not execute as it iss bcoz PVM remembers latest functionn definition only but not all bcoz PVM performss interpretation process.

def disp(a,b,c,d,e):    #function def-1
    print(a,b,c,d,e)
def disp(a,b,c,d):      #function def-2
    print(a,b,c,d)
def disp(a,b,c):        #function def-3
    print(a,b,c)
def disp(a,b):          #function def-4
    print(a,b)
def disp(a):            #function def-5
    print(a)
def disp():             #function def- 6
    print("Empty")

#main program
disp(10,20,30,40,50)
disp(10,20,30,40)
disp(10,20,30)
disp(10,20)
disp(10)
disp()