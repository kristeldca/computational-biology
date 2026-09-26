from pathlib import Path

file_path = Path("samples") / "010.txt"

dna_strings = []
profile = {
    "A": [],
    "C": [],
    "G": [],
    "T": []
}

n = 0

# Reads the given DNA strings from a file.
# DNA string can be multiple lines so we read each line
# and determine if it is part of the current string.
# We then save it to dna_strings list.
with open(file_path, "r") as file:
    lastStripped = ""
    for line in file:
        stripped = line.strip()
        if (stripped[0] == ">"):
            if (lastStripped != ""):
                dna_strings.append(lastStripped)
                n = len(lastStripped)
            lastStripped = ""
        else:
            lastStripped += stripped

    dna_strings.append(lastStripped)

# Initializes the matrix by setting the values to 0
def initialize_matrix():
    for base in profile:
        for i in range(n):
            profile[base].append(0)

# Initializes the profile matrix
def get_profile():
    initialize_matrix()
    for i in range(len(dna_strings)):
        for j in range(n):
            profile[dna_strings[i][j]][j] += 1

# Compares the profile to get the base with highest count.
# Returns the consensus - highest count for each index.   
def get_consensus():
    consensus = ""
    for i in range(n):
        max = 0
        max_base = ""
        for base in profile:
            if (profile[base][i] > max):
                max = profile[base][i]
                max_base = base
        consensus += max_base
    return consensus
                
get_profile()     
consensus = get_consensus()
print(consensus)
for base in profile:
    base_count = " ".join(map(str, profile[base]))
    print(f"{base}: {base_count}")