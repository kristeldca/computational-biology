# This function computes the  expected number of offspring
# displaying the dominant phenotype in the next generation,
# under the assumption that every couple has exactly two offspring.
# c1 - AA x AA = 100% chance = 2*1.0 = 2
# c2 - AA x Aa = 100% chance = 2*1.0 = 2
# c3 - AA x aa = 100% chance = 2*1.0 = 2
# c4 - Aa x Aa = 75% chance = 2*0.75 = 1.5
# c5 - Aa x aa = 50% chance = 2*0.5 = 1
# c6 - aa x aa = 0% chance = 2*0 = 0
def expected_dominant_offspring(counts):
    c1, c2, c3, c4, c5, c6 = counts
    
    total_expected = (2*c1) + (2*c2) + (2*c3) + (1.5*c4) + (1*c5) + (0*c6)
    
    return total_expected

given_str = input("Enter the number of couples in a population possessing each genotype pairing for a given factor: ")
given_counts = [int(x) for x in given_str.split()]
print(expected_dominant_offspring(given_counts))