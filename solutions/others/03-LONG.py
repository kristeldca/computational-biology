from pathlib import Path

script_path = Path(__file__).resolve()
root_path = script_path.parent.parent.parent
file_path = root_path / "samples" / "LONG.txt"

dna_strings = []

# Reads the DNA strings from a file.
# They are saved in the dna_strings list.
with open(file_path, "r") as file:
    lastStripped = ""
    for line in file:
        stripped = line.strip()
        if (stripped[0] == ">"):
            if (lastStripped != ""):
                dna_strings.append(lastStripped)
            lastStripped = ""
        else:
            lastStripped += stripped

    dna_strings.append(lastStripped)
    
# This function gets the max overlap of 2 strings by comparing
# the last x characters of string1 and first x characters of string2.
# The minimum overlap is half of the shorter string.
def get_max_overlap(str1, str2):
    max_length = min(len(str1), len(str2))
    min_overlap = (max_length // 2) + 1

    print(max_length, min_overlap)
    for i in range(max_length, min_overlap - 1, -1):
        if str1[-i:] == str2[:i]:
            return i
        
    return 0

# This function gets the superstring by iterating through the dna_strings list.
# If 2 strings has overlap, they are merged and removed from the list.
# The merged string will be added in the pool, replacing the 2 strings.
# The loop will end when 1 superstring is left.
def get_super_string():
    while len(dna_strings) > 1:
        merged_string = ""
        max_overlap_length = 0
        str1, str2 = "", ""
        
        for i in range(len(dna_strings)):
            for j in range(len(dna_strings)):
                if i != j:
                    overlap_length = get_max_overlap(dna_strings[i], dna_strings[j])
                    
                    if overlap_length > max_overlap_length:
                        max_overlap_length = overlap_length
                        str1, str2 = dna_strings[i], dna_strings[j]
                        merged_string = str1 + str2[overlap_length:]

        if max_overlap_length == 0:
            break
        else:
            print(f"str1: {str1} {max_overlap_length}")
            dna_strings.remove(str1)
            dna_strings.remove(str2)
            dna_strings.append(merged_string)
        
    return(dna_strings[0])

# print(dna_strings)
print(get_super_string())