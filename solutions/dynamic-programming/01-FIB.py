# This function implements fibonacci through recursion.
def fibonacci(count, sum, prev_sum):
    # If it is the last one, return the sum.
    # Else if it is the first one, default sum is one.
    # Else use the default sum + (k*prev_sum), then call the function again.
    if count == n-1:
        return sum
    elif count == 0:
        return fibonacci(count + 1, 1, 1)
    else:
        s = sum + (k*prev_sum)
        return fibonacci(count + 1, s, sum)


given = input("Enter two positive integers separated by space: ")
n, k = [int(x) for x in given.split()]
print (fibonacci(0, 0, 0))