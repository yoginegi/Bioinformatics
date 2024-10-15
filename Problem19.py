def find_neighbors(seq, max_mismatches):
    bases = ['A', 'C', 'G', 'T']

    if max_mismatches == 0:
        return {seq}

    if len(seq) == 0:
        return {""}

    neighbor_set = set()
    suffix_neighbors = find_neighbors(seq[1:], max_mismatches)

    for suffix in suffix_neighbors:
        if calculate_hamming_distance(seq[1:], suffix) < max_mismatches:
            for base in bases:
                neighbor_set.add(base + suffix)
        else:
            neighbor_set.add(seq[0] + suffix)

    return neighbor_set

def calculate_hamming_distance(str1, str2):
    return sum(1 for a, b in zip(str1, str2) if a != b)

input_pattern = "ATTCGCGT"
max_differences = 2

resulting_neighbors = find_neighbors(input_pattern, max_differences)
for neighbor in sorted(resulting_neighbors):
    print(neighbor)
