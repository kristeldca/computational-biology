from pathlib import Path

script_path = Path(__file__).resolve()
root_path = script_path.parent.parent.parent
file_path = root_path / "samples" / "SPLC.txt"

D = ""
I = []
isFirst = True

rna_codon_table = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G"
}

# Reads the given strings from a file.
# The first string is saved as the DNA string,
# while the rest are considered introns.
with open(file_path, "r") as file:
    lastStripped = ""
    for line in file:
        stripped = line.strip()
        if (stripped[0] == ">"):
            if (lastStripped != ""):
                if isFirst:
                    D = lastStripped
                    isFirst = False
                else:
                    I.append(lastStripped)
            lastStripped = ""
        else:
            lastStripped += stripped

    I.append(lastStripped)
    
# This function removes all the introns from the dna string.
def remove_introns(str, intron_list):
    for intron in intron_list:
        str = str.replace(intron, "")
        
    return str

# Changes all instances of "T" to "U"
# Returns the transcribed DNA
def transcribe_rna(str):
    rna = ""
    for base in str:
        if base == "T":
            base = "U"
        rna = rna + base
    return rna

# This function translates the RNA string to a protein string.
# The RNA string is grouped by 3 and gets the corresponding amino acid
# based on the RNA codon table.
def translate_to_protein_string(str):
    translated = ""
    chunks = [str[i:i+3] for i in range(0, len(str), 3)]
    for chunk in chunks:
        translated += (rna_codon_table.get(chunk, ""))
    return translated
     
# To get the protein string resulting from transcribing and translating the exons of s,
# the introns were removed from the DNA string first.
# Then the DNA is transcribed to RNA by replacing T with U.
# The resulting RNA is translated to protein.
dna_string = remove_introns(D, I)
rna_string = transcribe_rna(dna_string)
protein_string = translate_to_protein_string(rna_string)
print(protein_string)
