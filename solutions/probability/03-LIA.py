import math

# This function computes the probability that at least n Aa Bb organisms
# will belong to the k-th generation using Binomial distribution formula.
# Rounds off the probability to 3 decimal places.
def independent_alleles(k, n):
    # Total number of organisms in the k-th generation
    total_organisms = 2 ** k
    
    # Probability of a child being Aa Bb
    p_success = 0.25
    p_failure = 0.75
    
    probability = 0.0
    
    # Sum up probabilities from n to the maximum possible organisms
    for i in range(n, total_organisms + 1):
        # Binomial distribution formula: totalCi * p^i * q^(total-i)
        combinations = math.comb(total_organisms, i)
        prob_i = combinations * (p_success ** i) * (p_failure ** (total_organisms - i))
        probability += prob_i
        
    # Round to three decimal places
    return round(probability, 3)

given_str = input("Enter two positive integers separated by space: ")
given_counts = [int(x) for x in given_str.split()]
print(independent_alleles(given_counts[0], given_counts[1]))
