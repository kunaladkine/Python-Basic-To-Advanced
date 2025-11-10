a=10>2 or 20>30     #Short Circuit Evaluation
print(f"Value of A Will : {a}")

b=20>10 or 30>40 or 50>60       #Short Circuit Evaluation
print(f"Value of b will : {b}")

c=10>20 or 40>50 or 50>40   #Full Length Evaluation
print(f"Value of c will : {c}")

d=10>20 or 40>50 or 50>60       #Full Length Evaluation
print(f"Value of d will : {d}")
