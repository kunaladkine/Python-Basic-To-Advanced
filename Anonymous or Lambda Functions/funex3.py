#program for accepting list of numerical values and find bigest among them

findmax=lambda lst:max(lst)
findmin=lambda lst:min(lst)

#main program
print("enter list of values separated by space :")
lst=[float(val) for val in input().split()]
maxv=findmax(lst)
minv=findmin(lst)
print("max({})={}".format(lst,maxv))
print("min({})={}".format(lst,minv))