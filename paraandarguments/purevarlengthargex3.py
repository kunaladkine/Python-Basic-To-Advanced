#program for demonstrating the need of variable length arguments.
#this program will execute as it is

def disp(sno,sname,marks,*kvr,city="HYD"):
    print("Student Number:{}".format(sno))
    print("Student Name :{}".format(sname))
    print("Student Marks:{}".format(marks))
    print("Student City:{}".format(city))
    print("Variable Length Values:")
    s=0
    for val in kvr:
        print("\t\t{}".format(val))
        s=s+val
    print("_"*50)
    print("\tSum={}".format(s))
    print("_"*50)

#main program
disp(100,"RS",23.45,10,20,30,40,50)
disp(200,"RS",33.88,10,20,30,40)
disp(300,"TS",55.66,10,20,30)
disp(400,"EW",77.99,10,20)
disp(500,"TS",88.99,10)
disp(600,"OS",33.33)
