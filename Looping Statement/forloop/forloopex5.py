s="PYTHON"
print("By using for loop-forward direction without indices")
for ch in s:
    print("\t\t{}".format(ch))
print("---------------------------")
print("Backward direction without indices ")
for ch in s[::-1]:
    print(ch)
print("---------------------------")
print("forward direction with +ve indices.")
for index in range(len(s)):
    print("\t{}".format(s[index]))
print("-----------------------------")
print("Forward direction with -ve indices")
for index in range(-len(s),0):
    print("\t{}".format(s[index]))
print("-----------------------------")
print("backward direction with +ve indices")
for index in range(len(s)-1,-1,-1):
    print("\t{}".format(s[index]))
print("----------------------")
print("backward direction with -ve indices")
for index in range(-1,-(len(s)+1),-1):
    print("\t{}".format(s[index]))
print("------------------------")