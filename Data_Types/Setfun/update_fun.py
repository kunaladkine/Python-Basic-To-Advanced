#syntax : SetObj3=Setobj1.update(SetObj2)
#this function updates the elemetns of SetObj2 with setobj1 and placed all updated elements in setobj1 itself and never place the elements in setobj3.

s1={10,20,30}
s2={30,40,50}

s1.update(s2)           #updated element and unique take only at once
print(s1)

s3=s2.update(s1)            #gives none because it take itsself in s2
print(s3)

print(s2)

