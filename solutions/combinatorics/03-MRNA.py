# This function computes the number of possible combinations.
def infer_mrna_count(protein_string):
    # Number of codons that code for each amino acid
    codon_frequencies = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3, 
        'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6, 
        'T': 4, 'V': 4, 'W': 1, 'Y': 2
    }
    
    # Start with 3 because there are 3 possible STOP codons at the end
    total_combinations = 3 
    MOD = 1000000
    
    for amino_acid in protein_string:
        total_combinations = (total_combinations * codon_frequencies[amino_acid]) % MOD
        
    return total_combinations

P = input("Enter the protein string: ")
print(infer_mrna_count(P)) 
