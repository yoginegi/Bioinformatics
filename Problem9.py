def gc_content(dna):
    gc_count = dna.count('G') + dna.count('C')
    return (gc_count / len(dna)) * 100

def read_fasta(fasta_lines):
    fasta_data = {}
    label = ""
    sequence = ""

    for line in fasta_lines:
        line = line.strip()
        if line.startswith('>'):
            if label:
                fasta_data[label] = sequence
            label = line[1:]
            sequence = ""
        else:
            sequence += line

    if label:
        fasta_data[label] = sequence

    return fasta_data

with open("rosalind_gc.txt", "r") as file:
    fasta_lines = file.readlines()

fasta_data = read_fasta(fasta_lines)

highest_gc_content = 0
best_label = ""

for label, dna in fasta_data.items():
    gc_percentage = gc_content(dna)
    if gc_percentage > highest_gc_content:
        highest_gc_content = gc_percentage
        best_label = label

print(best_label)
print(f"{highest_gc_content:.6f}")
