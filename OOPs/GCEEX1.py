#Program for Demonstrating whether the GC is Running or Not
#GCEX1.py
import gc
print("Program Execution Started")
print("Initially, Is GC Running=",gc.isenabled())
a=10
b=20
c=a+b
gc.disable()
print("Now, Is GC Running=",gc.isenabled())
print("Val of a=",a)
print("Val of b=",b)
gc.enable()
print("Sum==",c)
print("Now, Is GC Running=",gc.isenabled())
print("Program Execution Ended")