import requests
import re
from pathlib import Path

script_path = Path(__file__).resolve()
root_path = script_path.parent.parent.parent
file_path = root_path / "samples" / "MPRT.txt"

protein_list = []
motif_pass = {}

# Reads the given UniProt Protein Database access IDs from a file
with open(file_path, "r") as file:
    for line in file:
        protein_list.append(line.strip())

# This function verifies if the protein possesses the N-glycosylation motif.
def verify_n_glycosylation_motif(accession: str, key_name: str):
    # Fetch the full JSON entry
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    # Gets the sequence.value from the JSON response
    sequence_data = data.get("sequence", {})
    sequence_string = sequence_data.get("value", "")
    
    # Finds matches based on N{P}[ST]{P} pattern
    if sequence_string:
        # Regex for  N{X}[ST]{X} where X is not P
        pattern = r'(?=(N[^P][ST][^P]))'
        motif_matches = [match.start() + 1 for match in re.finditer(pattern, sequence_string)]
        
        if motif_matches:
            motif_pass[key_name] = []
            for pos in motif_matches:
                motif_pass[key_name].append(pos)

# Verify each protein
for protein in protein_list:
    verify_n_glycosylation_motif(protein.split("_")[0], protein) 

for key, m in motif_pass.items():
    print(f"{key} ")
    print(" ".join(map(str, m)) + " ")
