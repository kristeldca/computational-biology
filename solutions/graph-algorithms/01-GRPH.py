from pathlib import Path

# Reads the given DNA strings from a file.
# DNA string can be multiple lines so we read each line
# and determine if it is part of the current string.
# We then save it to dna_strings object, and
# initializes with properties str itself, head, tail, and adjacents list.
file_path = Path("samples") / "012.txt"
dna_strings = {}
with open(file_path, "r") as file:
    lastStripped = ""
    for line in file:
        stripped = line.strip()
        if (stripped[0] == ">"):
            dna_strings[stripped[1:]] = {
                "str": "",
                "head": "",
                "tail": "",
                "adjacents": []
            }
            last_stripped = stripped[1:]
        else:
            dna_strings[last_stripped]["str"] += stripped

# This function initializes the head and tails of the string.
# head - first 3 characters of the string
# tail - last 3 characters of the string
def initialize_heads_and_tails():
    for dna_string in dna_strings.values():
        dna_string_length = len(dna_string["str"])
        dna_string["head"] = dna_string["str"][:3]
        dna_string["tail"] = dna_string["str"][(dna_string_length-3):]
        
# This functions scans through the dna_strings.
# If the tail matches the head, they are adjacents,
# and therefore added to the adjacents list.
def graph_adjacents():
    for tail_key, dna_string_tail in dna_strings.items():
        for head_key, dna_string_head in dna_strings.items():
            if (dna_string_tail["tail"] == dna_string_head["head"] and tail_key != head_key):
                dna_string_tail["adjacents"].append(head_key)
            
   
# Initializes the heads and tails first,
# then lists the adjacents.
initialize_heads_and_tails()
graph_adjacents()

# Prints the adjacents
for dna_string_key, dna_string in dna_strings.items():
    if len(dna_string["adjacents"]) > 0:
        for adjacent in dna_string["adjacents"]:
            print(dna_string_key, adjacent)