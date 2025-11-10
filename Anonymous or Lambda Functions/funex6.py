#program for accepting List of  Numerical values and Find Biggest among them
#AnonymousFunEx6.py
def kvrmax(lst): # Normal Function Def-lst=10 12 34 1 23 67 -12 4 5
    maxv=lst[0]
    for val in lst[1:]:
        if(val>maxv):
            maxv=val
    return maxv

def kvrmin(lst): # Normal Function Def
    minv = lst[0]
    for val in lst[1:]:
        if (val < minv):
            minv = val
    return minv

#Anonymous Function Defs
findmax=lambda lst:kvrmax(lst)
findmin=lambda lst:kvrmin(lst)

#main program
print("Enter List of Values separated by space:")
lst=[float(val) for val in input().split()]
maxv=findmax(lst)
minv=findmin(lst)
print("max({})={}".format(lst,maxv))
print("min({})={}".format(lst,minv))