#program for accepting list of numerical values and find biggest among them

def kvrmax(lst):
    maxv=lst[0]
    for val in lst:
        if(val>maxv):
            maxv=val
    return maxv

def kvrmin(lst):
    minv=lst[0]
    for val in lst:
        if(val<minv):
            minv=val
    return minv

#anonymous function defs
findmax=lambda lst:kvrmax(lst)
findmin=lambda lst:kvrmin(lst)

#main program
print("Enter List of Values separated by space :")
lst=[float(val) for val in input().split()]
maxv=findmax(lst)
minv=findmin(lst)
print("max({})={}".format(lst,maxv))
print("min({})={}".format(lst,minv))