def DNA_strand(dna):
    new_sentence = ''
    for letter in dna:
        if letter == 'A':
            new_sentence += 'T'
        if letter == 'T':
            new_sentence += 'A'
        if letter == 'C':
            new_sentence += 'G'
        if letter == 'G':
            new_sentence += 'C'
    return new_sentence
print(DNA_strand("ATTGC"))