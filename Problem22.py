def reverse_complement(pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complemented_pattern = ''

    for nucleotide in pattern:
        complemented_pattern += complement[nucleotide]

    reverse_complemented_pattern = complemented_pattern[::-1]

    return reverse_complemented_pattern

pattern = "AAAACCCGGT"
result = reverse_complement(pattern)
print(result)
