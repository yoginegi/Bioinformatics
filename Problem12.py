def Patterntonumber(Pattern):
    value = {"A": 0, "C": 1, "G": 2, "T": 3}
    number = 0

    for i in Pattern:
        number = number * 4 + value[i]

    return number

Pattern = "GCACTTATAAACGTAGAAAACTGATG"
print(Patterntonumber(Pattern))
