from pathlib import Path

# reads the given DNA string from a file
file_path = Path("samples") / "002.txt"
with open(file_path, "r") as file:
    t = file.read()

u = ""

# Changes all instances of "T" to "U"
# Returns the transcribed DNA
def transcribe_rna():
    global u
    for base in t:
        if base == "T":
            base = "U"
        u = u + base
    return t

transcribe_rna()
print(u)