# Contains the mapping of bases: A-T, C-G
pair_mapping = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

# Gets the pair of each base based on the pair_mapping
def reverse_dna(s):
    reverse = ""
    for base in s:
        if pair_mapping.get(base) is not None:
            reverse += pair_mapping[base]
    return "".join(reversed(reverse))

# Iterates through the DNA strings and gets the substrings with 4-12 length.
# Each substrings are being checked if the reverse complement is the same.
def get_reverse_palindromes(D):
    palindromes = []
    for i in range(len(D)-3):
        for j in range(4, 13):
            if i+j <= len(D):
                str = D[i:i+j]
                reverse_complement = reverse_dna(str)
                
                if str == reverse_complement:
                    palindromes.append({
                        "position": i+1,
                        "length": len(str),
                        "str": str,
                        "reverse_complement": reverse_complement,
                    })
                    
    return palindromes

dna_string = input("Enter the DNA string: ")
reverse_palindromes = get_reverse_palindromes(dna_string)

for rp in reverse_palindromes:
    print(f"{rp['position']} {rp['length']}")
