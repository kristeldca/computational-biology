from pathlib import Path

# Reads the given DNA string from a file
file_path = Path("samples") / "006.txt"
with open(file_path, "r") as file:
    a = file.readline().strip()
    b = file.readline().strip()

# This function goes through 2 strings to check
# if the character is different on a particular index.
# If the two strings are not of equal length,
# we do not proceed as it is an invalid input.
def get_hamming_distance():
    if (len(a) != len(b)):
        return "invalid input"
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            counter += 1
    return counter

print(get_hamming_distance())