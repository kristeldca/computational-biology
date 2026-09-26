from pathlib import Path

# Reads the given DNA string from a file
# The first line contains the DNA string
# and the second line contains the substring
# you are looking for.
file_path = Path("samples") / "009.txt"
with open(file_path, "r") as file:
    dna_string = file.readline().strip()
    substring = file.readline().strip()

# Gets all of the locations of the substring in the DNA string
# This uses the built-in string method .find()
def get_all_locations():
    locations = []
    start = 0

    while True:
        start = dna_string.find(substring, start)
        if start == -1:
            break
        locations.append(start + 1)
        start += 1
        
    return locations

all_locations = get_all_locations()
print(" ".join(map(str, all_locations)))