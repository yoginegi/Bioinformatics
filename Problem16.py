from collections import defaultdict
def search(inseq, k, L, t):
    lookup = defaultdict(list)
    result = set()

    for cursor in range(len(inseq) - k + 1):
        seg = inseq[cursor:cursor + k]

        while lookup[seg] and cursor + k - lookup[seg][0] > L:
            lookup[seg].pop(0)

        lookup[seg].append(cursor)
        if len(lookup[seg]) == t:
            result.add(seg)

    return result

genome = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
k = 5
L = 75
t = 4

clumps = search(genome, k, L, t)
print(" ".join(clumps))
