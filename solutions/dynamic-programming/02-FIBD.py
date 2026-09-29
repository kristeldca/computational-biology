sums = []

# Run for n months, rabbits die after m months.
# Uses recursion to list the number of rabbits per month.
def fibonacci(count, sum, prev_sum):
    # Base case: last one
    if count == n:
        return sum
    # Base case: first 2 months
    elif count < 2:
        sums.append(1)
        return fibonacci(count + 1, 1, 1)
    else:
        deaths = 0
        # Check the number of deaths
        # Base case is 1 death in the first 2 gens
        # Otherwise, subtract the number of born rabbits on count-m+1 months
        if count >= m:
            if count-(m+1) < 2:
                deaths = 1
            else:
                deaths = sums[count-(m+1)]

        s = sum + prev_sum - deaths
        sums.append(s)
        return fibonacci(count + 1, s, sum)


given = input("Enter two positive integers separated by space: ")
n, m = [int(x) for x in given.split()]
print (fibonacci(0, 0, 0))
print(sums)