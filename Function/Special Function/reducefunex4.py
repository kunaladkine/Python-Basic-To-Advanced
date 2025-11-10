#program for accepting list of words and merge them by using reduce()
#reducefunex4.py

import functools
print("Enter List of words separated by comma:")
lst=[str(val) for val in input().split(",")]
line=functools.reduce(lambda k,v:k+" "+v,lst)
print("Result Line:")
print(line)