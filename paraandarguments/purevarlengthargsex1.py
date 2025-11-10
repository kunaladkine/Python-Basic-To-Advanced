#program for demonstrating the need of variable length arguments

#this program will execute as it is
def disp(*kvr):
    print(kvr,type(kvr),len(kvr))

#main program
disp(10,20,30,40,50)    # Function Call-1 with 5 Possitional  Args
disp(10,20,30,40)       # Function Call-2 with 4 Possitional  Args
disp(10,20,30)          # Function Call-3 with 3 Possitional  Args
disp(10,20)             # Function Call-4 with 2 Possitional  Args
disp(10)                     # Function Call-5 with 1 Possitional  Args
disp()                       # Function Call-6 with 0 Possitional  Args

