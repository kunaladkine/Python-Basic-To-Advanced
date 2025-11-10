#Combination 'and' 'or' not operators

a=not(100 and 200)
print(f"The Result Will : {a}")

b=not 100 and not 200
print(f"The Result Will : {b}")

f=not 0 and not 200-200
print(f"The Result Will : {f}")

c=not(100 or 200)
print(f"The Result Will : {c}")

#tricky Question
e=(100 or 200)-1
print(f"The Result Will : {a}")

d=not(100 or 200)-1
print(f"the Result Will : {d}")