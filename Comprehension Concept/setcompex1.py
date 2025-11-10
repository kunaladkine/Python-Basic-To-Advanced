#program for obtaining +ve values and -ve values in separate lists

lst=[10,20,45,0,-8,99,66,54,-5]
print("Given List is =",lst)
pglist={val for val in lst if val>0}
nglist={val for val in lst if val<0}
print("Positive Value List =",pglist)
print("Negative Value List=",nglist)