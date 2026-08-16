# ------------------------------------------------------------
# Program: Prime Numbers in a Range
# Author: Mohnish Rawat
# Description:
#   This program prints all prime numbers between two given numbers.
#   Example: Range 10 to 20 → 11, 13, 17, 19
# ------------------------------------------------------------

n = int(input("Enter a 1st number: "))   # Take first number as input
m = int(input("Enter a 2nd number: "))   # Take second number as input

# ------------------------------------------------------------
# Loop through all numbers in the range [n, m]
# ------------------------------------------------------------
for i in range(n, m + 1):                # Iterate from n to m (inclusive)
    isprime = True                       # Assume current number is prime

    # ------------------------------------------------------------
    # Check divisibility of i
    # ------------------------------------------------------------
    for j in range(2, i):                # Test divisors from 2 up to i-1
        if i % j == 0:                   # If divisible by j
            isprime = False              # Mark as not prime
            break                        # Exit inner loop early

    # ------------------------------------------------------------
    # Print prime numbers
    # ------------------------------------------------------------
    if isprime and i > 1:                # Exclude 1 (not prime)
        print(i)
