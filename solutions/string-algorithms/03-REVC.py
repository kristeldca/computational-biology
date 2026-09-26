from pathlib import Path

# reads the given DNA string from a file
file_path = Path("samples") / "003.txt"
with open(file_path, "r") as file:
    s = file.read()

# Contains the mapping of bases: A-T, C-G
pair_mapping = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

# Gets the pair of each base based on the pair_mapping
def reverse_dna():
    reverse = ""
    for base in s:
        if pair_mapping.get(base) is not None:
            reverse += pair_mapping[base]
    return reverse

# Reverses the converted string
sc = "".join(reversed(reverse_dna()))
print (sc)
    