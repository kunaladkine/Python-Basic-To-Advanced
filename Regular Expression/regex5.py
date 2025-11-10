#program to find except a , b ,c
import re
gd="cKj5%H2NqbY@8aDmAEj9!BzC"
sp="[^abc]"
matter=re.finditer(gd,sp)
for mat in matter:
    print(" Start Index {} End Index {} Value {}".format(mat.group(),mat.start().mat.end(),mat.group()))
    print("_"*50)