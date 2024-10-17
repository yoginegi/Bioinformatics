from collections import defaultdict

def hamming_distance(s1, s2):
    mismatches = 0
    for a, b in zip(s1, s2):
        if a != b:
            mismatches += 1
    return mismatches


def generate_neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    neighbors = set()
    suffix = pattern[1:]
    for neighbor in generate_neighbors(suffix, d):
        for base in 'ACGT':
            if hamming_distance(suffix, neighbor) < d:
                neighbors.add(base + neighbor)
            else:
                neighbors.add(pattern[0] + neighbor)
    return neighbors


def count_occurrences(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i + len(pattern)]
        if hamming_distance(pattern, substring) <= d:
            count += 1
    return count


def frequent_words_with_mismatches(text, k, d):
    count_dict = defaultdict(int)

    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]  # Get the k-mer
        for neighbor in generate_neighbors(kmer, d):
            count_dict[neighbor] += 1  # Count the k-mer and its neighbors

    max_count = max(count_dict.values())  # Find the maximum count
    most_frequent_kmers = [kmer for kmer, count in count_dict.items() if count == max_count]

    return most_frequent_kmers

text = "GTGCGTCTGACCCCCAAACCGGAACCTACCCCCAAATTGTAGCCCACCGGAACCTATTGTAGCCCACCCCCAAAGTGCGTCTGAGTGCGTCTGACCCCCAAAGTATCCCTAGTGCGTCTGAGTGCGTCTGAGTATCCCTACCCCCAAATTGTAGCCCACCCCCAAAGTGCGTCTGAGTATCCCTAGTGCGTCTGACCCCCAAAGTATCCCTACCGGAACCTACCGGAACCTACCCCCAAAGTATCCCTACCCCCAAATTGTAGCCCAGTATCCCTACCGGAACCTAGTGCGTCTGAGTGCGTCTGAGTATCCCTACCGGAACCTACCGGAACCTACCGGAACCTATTGTAGCCCATTGTAGCCCAGTATCCCTATTGTAGCCCACCCCCAAACCCCCAAACCCCCAAATTGTAGCCCATTGTAGCCCACCCCCAAATTGTAGCCCAGTGCGTCTGACCCCCAAACCGGAACCTAGTATCCCTAGTATCCCTACCGGAACCTATTGTAGCCCACCCCCAAATTGTAGCCCAGTATCCCTATTGTAGCCCACCGGAACCTATTGTAGCCCATTGTAGCCCACCGGAACCTACCCCCAAATTGTAGCCCAGTGCGTCTGAGTGCGTCTGAGTGCGTCTGACCGGAACCTACCCCCAAAGTGCGTCTGATTGTAGCCCACCGGAACCTACCCCCAAACCCCCAAAGTATCCCTACCGGAACCTACCGGAACCTAGTATCCCTAGTGCGTCTGAGTATCCCTATTGTAGCCCAGTATCCCTAGTATCCCTAGTATCCCTACCCCCAAAGTATCCCTAGTATCCCTATTGTAGCCCAGTATCCCTAGTATCCCTATTGTAGCCCACCGGAACCTACCCCCAAAGTGCGTCTGATTGTAGCCCATTGTAGCCCAGTGCGTCTGACCGGAACCTACCCCCAAATTGTAGCCCAGTGCGTCTGAGTATCCCTACCCCCAAATTGTAGCCCA"
k = 5
d = 3

result = frequent_words_with_mismatches(text, k, d)
print(" ".join(result))
