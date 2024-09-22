with open("rosalind_ini5.txt", 'r') as ip:
    lines = ip.readlines()

with open("rosalind_ini5.txt", 'w') as op:
    for i in range(len(lines)):
        if (i + 1) % 2 == 0:
            op.write(lines[i])
