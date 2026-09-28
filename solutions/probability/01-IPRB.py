from pathlib import Path

# Reads the given from the file
# k - no of individuals that are homozygous dominant
# m - no of individuals that are heterozygous
# n - no of individuals that are homozygous recessive
file_path = Path("samples") / "007.txt"
with open(file_path, "r") as file:
    k, m, n = [int(x) for x in file.readline().split(" ")]

# Computes the possible number of recessive outcomes
# Heterozygous × Heterozygous Aa x Aa = 25% chance
# Heterozygous × Homozygous Recessive Aa x aa or aa x Aa = 50% chance
# Homozygous Recessive × Homozygous Recessive aa x aa = 100% chance
def get_recessive_outcomes():
    return 0.25*m*(m-1) + m*n + n*(n-1)

# Computes the total number of possible pairs
# total_number_of_individuals*(total_number_of_individuals-1)
def get_total_pairs():
    return (k+m+n)*(k+m+n-1)

# Dominant outcome = 1 - recessive outcome
recessive_probability = get_recessive_outcomes()/get_total_pairs()
print(f"{(1-recessive_probability):.5f}")