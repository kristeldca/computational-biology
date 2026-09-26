from pathlib import Path

# reads the given DNA string from a file
file_path = Path("samples") / "001.txt"
with open(file_path, "r") as file:
    data_set = file.read()

# counts the character provided from the file
def get_character_count(character):
    return data_set.count(character)

# gets the count of each nucleobase
def count_dna_nucleotides():
    return get_character_count("A"), get_character_count("G"), get_character_count("C"), get_character_count("T")

count_dna_nucleotides()