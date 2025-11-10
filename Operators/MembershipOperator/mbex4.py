# Membership + Bitwise Complement Program
numbers = [5, 10, 15, 20, 25, 30]
u_num = int(input("Enter The Value : "))

if u_num in numbers:
    print("✅ Number Found in the List")
    print("--------------- Operations ---------------")

    print(f"➤ Bitwise Complement (~{u_num}) : {~u_num}")
    print(f"➤ Binary of {u_num:<3}             : {bin(u_num)}")
    print(f"➤ Binary of ~{u_num:<3}            : {bin(~u_num)}")
else:
    print("❌ Number Not Found")
