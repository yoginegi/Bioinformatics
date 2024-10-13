def minimum_skew(genome):
    skew = [0]

    for i in range(len(genome)):
        if genome[i] == 'G':
            skew.append(skew[-1] + 1)
        elif genome[i] == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])

    min_skew = min(skew)
    min_positions = [i for i, val in enumerate(skew) if val == min_skew]

    return min_positions


genome = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
min_skew_positions = minimum_skew(genome)
print(" ".join(map(str, min_skew_positions)))

