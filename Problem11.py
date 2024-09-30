Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

counts = {}

for i in range(len(Text)- k +1):
    kmer = Text[i : i+ k]
    if kmer in counts:
        counts[kmer] += 1
    else:
        counts[kmer] = 1

max_count = max(counts.values())

most_frequent_kmers = []
for kmer, count in counts.items():
    if count == max_count:
        most_frequent_kmers.append(kmer)

print(" ".join(most_frequent_kmers))


