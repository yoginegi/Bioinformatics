from collections import defaultdict

def hamming_distance(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

def generate_neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighbors = set()
    suffix_neighbors = generate_neighbors(pattern[1:], d)
    for neighbor in suffix_neighbors:
        for base in 'ACGT':
            if hamming_distance(pattern[1:], neighbor) < d:
                neighbors.add(base + neighbor)
            else:
                neighbors.add(pattern[0] + neighbor)
    return neighbors

def reverse_complement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[n] for n in reversed(pattern))

def frequent_words_with_mismatches_and_reverse_complements(text, k, d):
    count_dict = defaultdict(int)
    
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        reverse_kmer = reverse_complement(kmer)
        
        for neighbor in generate_neighbors(kmer, d):
            count_dict[neighbor] += 1
        for reverse_neighbor in generate_neighbors(reverse_kmer, d):
            count_dict[reverse_neighbor] += 1
    
    max_count = max(count_dict.values())
    most_frequent_kmers = [kmer for kmer, count in count_dict.items() if count == max_count]
    
    return most_frequent_kmers

text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

result = frequent_words_with_mismatches_and_reverse_complements(text, k, d)
print("Most frequent k-mers with mismatches and reverse complements:", " ".join(result))
