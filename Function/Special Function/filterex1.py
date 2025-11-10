from selectors import SelectSelector


def positive(val):
    if(val>0):
        return True
    else:
        return False

def negative(val):
    return True if val<0 else False

#main program
lst=[10,3,0,45,-8,-9,-8,-4,44]
plist=filter(positive,lst)
nlist=filter(negative,lst)
print("Positive Value:",list(plist))
print("Negative Value :",list(nlist))
#when we display an object of filter, we are geetting its memeory address., so get its content filter object.
#we must typecast to any iterable object.

