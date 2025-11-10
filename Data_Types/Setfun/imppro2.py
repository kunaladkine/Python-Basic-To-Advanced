# Consider the Following Problem:
Set_of_Music_Lovers = {"Alice", "Bob", "Charlie", "David"}
Set_of_Dance_Lovers = {"Charlie", "Eva", "Alice", "Frank"}

# Answer the Following Questionnaire:

# Q1. Find the names of people who love both Music and Dance.
bothmldl=Set_of_Music_Lovers.intersection(Set_of_Dance_Lovers)
print(bothmldl)

bothmldl=Set_of_Music_Lovers&Set_of_Dance_Lovers  #using the bitwise
print(bothmldl)

# Q2. Find the names of people who love only Music but not Dance.
onlyml=Set_of_Music_Lovers.difference(Set_of_Dance_Lovers)
print(onlyml)

onlyml=Set_of_Music_Lovers-Set_of_Dance_Lovers
print(onlyml)

# Q3. Find the names of people who love only Dance but not Music.
onlydl=Set_of_Dance_Lovers.difference(Set_of_Music_Lovers)
print(onlydl)

onlydl=Set_of_Dance_Lovers-Set_of_Music_Lovers
print(onlydl)

# Q4. Find the names of people who love either Music or Dance but not both (i.e. exclusive).
exclmldl=Set_of_Music_Lovers.symmetric_difference(Set_of_Dance_Lovers)
print(exclmldl)

exclmldl=Set_of_Music_Lovers^Set_of_Dance_Lovers
print(exclmldl)

# Q5. Find the names of people who love both or either of the hobbies (Music or Dance) — i.e., union of both sets.
bothmldl=Set_of_Dance_Lovers.union(Set_of_Music_Lovers)
print(bothmldl)

bothmldl=Set_of_Dance_Lovers|Set_of_Music_Lovers
print(bothmldl)