# Python program to print odd numbers in a List

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddlist = [val for val in lst if val % 2 != 0]
print("Odd List Is : ")
print(oddlist)

oddlist2=[val for val in lst[0::2]]
print(oddlist2)

for i in lst:
    if(i%2!=0):
        print(i,end=" ")

