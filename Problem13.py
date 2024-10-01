def Numbertopattern(number, k):
    value = {0: "A", 1: "C", 2: "G", 3: "T"}
    pattern = ""

    for i in range(k):
        remainder = number % 4
        pattern = value[remainder] + pattern
        number = number// 4

    return(pattern)

print(Numbertopattern(8378,8))
