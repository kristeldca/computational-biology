from pathlib import Path

file_path = Path("samples") / "014.txt"

dna_strings = []
str_length = 0

# Reads the given DNA strings from a file.
# DNA string can be multiple lines so we read each line
# and determine if it is part of the current string.
# We then save it to dna_strings list.
with open(file_path, "r") as file:
    last_stripped = ""
    for line in file:
        stripped = line.strip()
        if (stripped[0] == ">"):
            if (not(last_stripped == "")):
                dna_strings.append(last_stripped)
                last_stripped = ""
        else:
            last_stripped += stripped

    dna_strings.append(last_stripped)
    str_length = len(last_stripped)

# Returns the substrings
def substr_map(text: str, k: int):
    frequency_map = []

    for i in range(len(text)-k+1):
        str = text[i:i+k]

        if not(str in frequency_map):
            frequency_map.append(str)
        
    return frequency_map

# Gets the common substrings from the first 2 strings
# Checks which common substring from the first 2
#   are also on the rest of the strings starting from the longest
# Breaks the loop if it is not found from one of the strings
# Breaks the loop once the common string was found
def common_pattern():
    pattern = None
    intersections = []
    for i in range(str_length - 1, 1, -1):
        arrays = []
        for j in range(2):
            arrays.append(substr_map(dna_strings[j], i))

        intersection = list(set(arrays[0]).intersection(*arrays[1:]))

        if (len(intersection) > 0):
            intersections.append(intersection)

    common = ""
    for i in range(len(intersections)):
        not_found = False
        for j in range(len(intersections[i])):
            for k in range(len(dna_strings)):
                if not(intersections[i][j] in dna_strings[k]):
                    not_found = True
                    break

            if (not not_found):
                common = intersections[i][j]
                break

        if common != "":
            break
        
    return common

print(common_pattern())