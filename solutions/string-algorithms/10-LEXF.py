import itertools
from pathlib import Path

script_path = Path(__file__).resolve()
root_path = script_path.parent.parent.parent
file_path = root_path / "samples" / "LEXF.txt"

string_list = []
size = 0

# Reads the given strings from a file.
# The first line is saved as string_list by splitting the string by space.
# The second line is saved as the size.
with open(file_path, "r") as file:
    string_list = file.readline().strip().split(" ")
    size = int(file.readline().strip())

# Use itertools to get all combinations
combinations = itertools.product(string_list, repeat=size)

for x in combinations:
    print("".join(x))