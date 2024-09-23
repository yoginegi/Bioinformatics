s = "DNA String"

count_A = 0
count_C = 0
count_G = 0
count_T = 0

for char in s:
    if char == 'A':
        count_A += 1
    elif char == 'C':
        count_C += 1
    elif char == 'G':
        count_G += 1
    elif char == 'T':
        count_T += 1

print(count_A, count_C, count_G, count_T)
