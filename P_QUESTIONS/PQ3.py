val=int(input("Enter The Value : "))
# print("You Entered Value : ",val)
bit_val=int(input("Enter The Bit Value :"))
# print("You Enter Bit Value : ",bit_val)
print("--------------------------------------")

#left shift
left_shift=(val<<bit_val)
#right shift
right_shift=(val>>bit_val)

print(f"left shift : {left_shift}\nRight shift : {right_shift}")

#converted to binary
#binary form of left shift
left_bin=bin(left_shift)

#binary form of right shift
right_bin=bin(right_shift)
print("------------Conversion-----------------")
print(f"Original Number             :  {val}")
print("Binary Form of left Shift   : ",left_bin)
print("Binary Form of Right Shift  : ",right_bin)


'''
a = int(input("Enter an integer: "))

left_shift = a << 2
right_shift = a >> 2

print("Original number       :", a)
print("Binary (original)     :", bin(a))

print("\nAfter Left Shift (<<2):", left_shift)
print("Binary (left shift)   :", bin(left_shift))

print("\nAfter Right Shift (>>2):", right_shift)
print("Binary (right shift)  :", bin(right_shift))
'''