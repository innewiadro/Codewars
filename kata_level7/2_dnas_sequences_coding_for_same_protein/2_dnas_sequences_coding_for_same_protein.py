def code_for_same_protein(seq1,seq2):
    def translate(dna):
        return [
            codons[dna[i:i+3]]
            for i in range(0, len(dna), 3)
        ]

    return translate(seq1) == translate(seq2)
