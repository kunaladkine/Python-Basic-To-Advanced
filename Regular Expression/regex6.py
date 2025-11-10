#program to find capital A,B and C
import re
gd="cKj5%H2NqbY@8aDmAEj9!BzC"
sp="[A-Z]"
matter=re.finditer(sp,gd)
for mat in matter:
    print("Start index {} End Index {} Value of {}".format(mat.start(),mat.end(),mat.group()))
    print("_"*50)