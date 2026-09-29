all_combinations = []

# Uses Heap's Algorithm to get all permutations
def get_permutation_of_n(arr, n):
    # Base case: if size is 1, we found a complete arrangement
    if n == 1:
        all_combinations.append(" ".join(arr))
        return

    for i in range(n):
        get_permutation_of_n(arr, n - 1)

        # If size is odd, swap the first and last element
        # If size is even, swap the i-th and last element
        if n % 2 == 1:
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
        else:
            arr[i], arr[n - 1] = arr[n - 1], arr[i]

try:
    size = int(input("Enter the size: "))
    arr = []
    for i in range(size):
        arr.append(str(i+1))
        
    get_permutation_of_n(arr, size)

    print(len(all_combinations))

    all_combinations.sort()
    for i in range(len(all_combinations)):
        print(all_combinations[i])
except ValueError:
    print("Invalid input! Please enter a whole number.")