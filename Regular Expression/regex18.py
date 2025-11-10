import re
gd="cKj5%H2NqbY@8aDmAEj9!BzC"
sp=r"\w"
matter=re.finditer(sp,gd)
for mat in matter:
    print("Index of {} Start Index {} End Indexx {} Value of {}".format(mat.group(),mat.start(),mat.end(),mat.group()))
    print("_"*50)