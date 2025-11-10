# Syntax1:    ListObj.sort()
# Syntax2:    ListObj.sort(reverse=False)
# Syntax3:   ListObj.sort(reverse=True)


lst=[10,20,30,-2,-5,1,0,5]
print(lst)

lst.sort()          #arrange the list in order
print(lst)

lst.reverse()   #reverse the list
print(lst)
            #OR
lst.sort(reverse=True)
print(lst)

lst.sort(reverse=False)
print(lst)