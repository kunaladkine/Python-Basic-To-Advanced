#program for searching either 'a' or 'b' or 'c' only
import re
gd="cKj5%H2NqbY@8aDmAEj9!BzC"
sp="[abc]"
matter=re.finditer(sp,gd)
for mat in matter:
    print("_"*50)
    print("Start Index {} End Index {} Value {}".format(mat.start(),mat.end(),mat.group()))
    print("_"*50)