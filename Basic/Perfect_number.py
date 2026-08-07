# ------------------------------------------------------------
# Program: Perfect Number Checker
# Author: Mohnish Rawat
# Description:
#   A perfect number is a positive integer that is equal to the sum
#   of its proper divisors (excluding itself).
#   Example: 28 → 1 + 2 + 4 + 7 + 14 = 28
# ------------------------------------------------------------

n = int(input("Enter a number: "))  # Take input from user and convert it to integer
total = 0  # Initialize variable to store sum of divisors

# ------------------------------------------------------------
# Loop through all possible divisors up to n//2
# (No divisor can be greater than n/2 except n itself)
# ------------------------------------------------------------
for i in range(1, n // 2 + 1):  # Iterate from 1 to n//2
    if n % i == 0:  # If i divides n evenly
        total += i  # Add i to total sum of divisors

# ------------------------------------------------------------
# Compare sum of divisors with original number
# ------------------------------------------------------------
if total == n:  # If sum equals the number
    print("-----Number is perfect-----")  # Then it's a perfect number
else:
    print("-----Number is not perfect-----")  # Otherwise, not perfect
