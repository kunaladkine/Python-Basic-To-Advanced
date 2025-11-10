n = int(input("Enter Any Integer Number: "))

if n <= 0:
    print("{} is an Invalid Number.".format(n))
else:
    print("_" * 50)
    print("\tEven Numbers in Reverse Order up to {}".format(n))
    print("_" * 50)
    i = n
    ec = 0  # Even count
    es = 0  # Even sum

    while i > 0:
        if i % 2 == 0:
            print("\t{}".format(i))
            ec += 1
            es += i
        i -= 1
    else:
        print("_" * 50)
        print("\tTotal Even Count: {}".format(ec))
        print("\tSum of Even Numbers: {}".format(es))
        print("Program Executed Successfully.")
