# ------------------------------------------------------------
# Program: Prime Number Checker
# Author: Mohnish Rawat
# Description:
#   This program checks whether a given integer is prime.
#   A prime number is a natural number greater than 1 that has
#   no positive divisors other than 1 and itself.
#   Special Case: 1 is neither prime nor composite.
#   Example:
#     Input: 7 → Output: Prime Number
#     Input: 9 → Output: Not Prime Number
# ------------------------------------------------------------


n = int(input("Enter a number: "))  # Take input from user and convert it to an integer

if n == 1:  # Special case: 1 is neither prime nor composite
    print("----Neither prime nor composite----")
else:
    is_prime = True  # Assume the number is prime at the start

    # ------------------------------------------------------------
    # Loop to check divisibility
    # ------------------------------------------------------------
    for i in range(2, n):  # Iterate from 2 up to n-1
        if n % i == 0:  # If n is divisible by i (no remainder)
            is_prime = False  # Then it's not prime
            break  # Exit loop early since we found a divisor

    # ------------------------------------------------------------
    # Final decision based on flag
    # ------------------------------------------------------------
    if is_prime:  # If no divisor was found
        print("----Prime Number----")  # Confirm it's prime
    else:
        print("----Not Prime Number----")  # Otherwise, not prime
