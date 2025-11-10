#program for accepting a Digit and Display Its Name
d=int(input("Enter Any Digit:")) #1 2 3 4 5 6 7 8 9
if(d==0):
    print("{} is Zero".format(d))
else:
    if(d==1):
        print("{} is One".format(d))
    else:
        if(d==2):
            print("{} is TWO".format(d))
        else:
            if(d==3):
                print("{} is Three".format(d))
            else:
                if(d==4):
                    print("{} is Four".format(d))
                else:
                    if(d==5):
                        print("{} is Five".format(d))
                    else:
                        if(d==6):
                            print("{} is Six".format(d))
                        else:
                            if(d==7):
                                print("{} is Seven".format(d))
                            else:
                                if(d==8):
                                    print("{} is Eight".format(d))
                                else:
                                    if(d==9):
                                        print("{} is Nine")
                                    else:
                                        if(d>0):
                                            print("It is + Ve Number")
                                        else:
                                            if(d<0):
                                                print("It is -Ve Number.")
print("Program Executed Completed.")


