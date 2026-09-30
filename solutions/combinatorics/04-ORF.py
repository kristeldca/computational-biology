# Standard DNA codon table mapping to amino acids
# 'Stop' is marked with an asterisk '*'
codon_table = {
    "GCA": "A",
    "GCC": "A",
    "GCG": "A",
    "GCT": "A",
    "AGA": "R",
    "AGG": "R",
    "CGA": "R",
    "CGC": "R",
    "CGG": "R",
    "CGT": "R",
    "AAC": "N",
    "AAT": "N",
    "GAC": "D",
    "GAT": "D",
    "TGC": "C",
    "TGT": "C",
    "CAA": "Q",
    "CAG": "Q",
    "GAA": "E",
    "GAG": "E",
    "GGA": "G",
    "GGC": "G",
    "GGG": "G",
    "GGT": "G",
    "CAC": "H",
    "CAT": "H",
    "ATA": "I",
    "ATC": "I",
    "ATT": "I",
    "CTA": "L",
    "CTC": "L",
    "CTG": "L",
    "CTT": "L",
    "TTA": "L",
    "TTG": "L",
    "AAA": "K",
    "AAG": "K",
    "ATG": "M",
    "TTC": "F",
    "TTT": "F",
    "CCA": "P",
    "CCC": "P",
    "CCG": "P",
    "CCT": "P",
    "AGC": "S",
    "AGT": "S",
    "TCA": "S",
    "TCC": "S",
    "TCG": "S",
    "TCT": "S",
    "ACA": "T",
    "ACC": "T",
    "ACG": "T",
    "ACT": "T",
    "TGG": "W",
    "TAC": "Y",
    "TAT": "Y",
    "GTA": "V",
    "GTC": "V",
    "GTG": "V",
    "GTT": "V",
    "TAA": "*",
    "TAG": "*",
    "TGA": "*"
}

# Contains the mapping of bases: A-T, C-G
pair_mapping = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

# Gets the pair of each base based on the pair_mapping
def get_reverse_complement(s):
    x = ""
    for base in s:
        if pair_mapping.get(base) is not None:
            x += pair_mapping[base]
    return "".join(reversed(x))

# This function translates to ORF.
# Returns none if it does not reach a stop codon.
def translate_orf(dna_sequence, start_index):
    protein = []
    
    # Read by 3 from the start index
    # Stop on *
    for i in range(start_index, len(dna_sequence) - 2, 3):
        codon = dna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, '')
        
        if amino_acid == '*': 
            return "".join(protein)
        else:
            protein.append(amino_acid)
  
    return None 

# This function gets every distinct candidate protein string
# that can be translated from ORFs of s.
# This uses set so the elements will be unique.
def find_all_proteins(dna_sequence):
    candidate_proteins = set()
    strands = [dna_sequence, get_reverse_complement(dna_sequence)]
    
    for strand in strands:
        # Scan for Start codon (ATG)
        for i in range(len(strand) - 2):
            if strand[i:i+3] == 'ATG':
                protein = translate_orf(strand, i)
                if protein:
                    candidate_proteins.add(protein)
                    
    return list(candidate_proteins)

dna_string = input("Enter the DNA string: ")
proteins = find_all_proteins(dna_string)

for p in proteins:
    print(p)
