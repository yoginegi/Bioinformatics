def GenerateArray(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k - 1):
        array = [i + j for i in array for j in bases]
    return array

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

def ComputingFrequencyArray(text, k):
    k_mers = GenerateArray(k)
    frequency_array = []

    for pattern in k_mers:
        frequency_array.append(PatternCount(text, pattern))

    print(" ".join(map(str, frequency_array)))
    return frequency_array

text = "ACGCGGCTCTGAAA"
k = 2

ComputingFrequencyArray(text, k)
