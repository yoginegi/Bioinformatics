def hamming_distance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance

p = "GGGCCGTTGGT"
q = "GGACCGTTGAC"

result = hamming_distance(p, q)
print(result)
