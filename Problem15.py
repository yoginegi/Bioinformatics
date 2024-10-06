def PatternMatching(Pattern, Genome):
    occurrence = []

    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i + len(Pattern)] == Pattern:
            occurrence.append(i)

    return occurrence

Pattern = "ATAT"
Genome = "GATATATGCATATACTT"

result = PatternMatching(Pattern, Genome)
print(" ".join(map(str, result)))
