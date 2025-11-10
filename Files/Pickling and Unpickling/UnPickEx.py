#program for reading the employee record from file
#where ti contains employee record-emp.pick by using un-pickling process.

import pickle
def readrecords():
    with open("emp.pick","rb")as fp:
        print("_"*50)
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="  ")
                print()
            except EOFError:
                print("_"*50)
                break

#main program
readrecords()           #Function call