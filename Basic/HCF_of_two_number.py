# ------------------------------------------------------------
# Program: HCF (Highest Common Factor) using Euclidean Algorithm
# Author: Mohnish Rawat
# Description:
#   This program calculates the HCF (also called GCD) of two integers.
#   The Euclidean Algorithm works by repeatedly replacing the larger
#   number with the remainder until the remainder becomes zero.
#   Example: HCF of 48 and 18 → 6
# ------------------------------------------------------------

a = int(input("Enter value of A: "))   # Take first number as input
b = int(input("Enter value of B: "))   # Take second number as input

# ------------------------------------------------------------
# Euclidean Algorithm loop
# ------------------------------------------------------------
while b != 0:                          # Continue until remainder becomes zero
    a, b = b, a % b                    # Update: a becomes b, b becomes remainder

# ------------------------------------------------------------
# Print the final HCF
# ------------------------------------------------------------
print(a)                               # When loop ends, 'a' holds the HCF
