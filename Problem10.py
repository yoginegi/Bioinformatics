def PatternCount(Text, Pattern):
    count = 0
    pattern_length = len(Pattern)

    for i in range(len(Text) - pattern_length + 1):
        if Text[i:i + pattern_length] == Pattern:
            count += 1

    return count

Text = "GCGCG"
Pattern = "GCG"

print(PatternCount(Text, Pattern))
