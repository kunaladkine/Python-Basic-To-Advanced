#program fro obtaining +ve and -ve values in separate lists

lst=[10,20,-30,-40,50,60,-15,0,25]
print("Given Values=",lst)
pslist=[val for val in lst if val>0]
nglist=[val for val in lst if val<0]
print("Positive list=",pslist)
print("negative List=",nglist)

