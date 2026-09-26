from pathlib import Path

# Reads the given DNA strings from a file.
# DNA string can be multiple lines so we read each line
# and determine if it is part of the current string.
# We then save it to dna_strings object.
file_path = Path("samples") / "005.txt"
dna_strings = {}
with open(file_path, "r") as file:
    lastStripped = ""
    for line in file:
        stripped = line.strip()
        if (stripped[0] == ">"):
            dna_strings[stripped] = ""
            last_stripped = stripped
        else:
            dna_strings[last_stripped] += stripped

# ==============================================================================
# FUNCTION: get_character_count
# Description: Counts the occurrences of a target character inside a dataset.
#
# Parameters:
#   str (str): The DNA string
#   character (str): The specific target character or nucleobase
#                    to count (e.g., 'A', 'C', 'G', 'T').
#
# Returns:
#   int: The total count frequency of the character found within the dataset.
# ==============================================================================
def get_character_count(str, character):
    return str.count(character)

# ==============================================================================
# FUNCTION: get_gc_content
# Description: Counts the occurrences of C and G and divides it by the total
#   length of the string to get the percentage.
#
# Parameters:
#   str (str): The DNA string
#
# Returns:
#   float: The gc content of the DNA string in decimal form.
# ==============================================================================
def get_gc_content(str):
    c_count = get_character_count(str, "C")
    g_count = get_character_count(str, "G")
    gc_count = c_count + g_count
    return gc_count/len(str)

# ==============================================================================
# FUNCTION: get_highest_gc_content
# Description: Computes the gc content of each DNA string
#   and determines the largest value.
#
# Returns:
#   dict: The DNA string with the largest GC content - 
#         containing the key and GC content.
# ==============================================================================
def get_highest_gc_content():
    largest = { "key": "", "value": 0}
    for key, value in dna_strings.items():
        gc_content = get_gc_content(value)
        if (gc_content > largest["value"]):
            largest = {
                "key": key,
                "value": gc_content
            }
    return largest
            
highest_gc_content = get_highest_gc_content()
highest_gc_content_key = highest_gc_content["key"]
highest_gc_content_value = highest_gc_content["value"]
print(highest_gc_content_key[1:])
# Convert the decimal value to percentage
print(f"{highest_gc_content_value*100:.6f}")
