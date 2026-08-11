# ------------------------------------------------------------
# Program: LCM (Lowest Common Multiple) using HCF
# Author: Mohnish Rawat
# Description:
#   This program calculates the LCM of two integers.
#   Formula: LCM(a, b) = (a × b) / HCF(a, b)
#   Example: LCM of 12 and 18 → 36
# ------------------------------------------------------------

def hcf(a, b):
    # ------------------------------------------------------------
    # Function to calculate HCF using Euclidean Algorithm
    # ------------------------------------------------------------
    while b != 0:                     # Continue until remainder becomes zero
        a, b = b, a % b               # Update: a becomes b, b becomes remainder
    return a                          # When loop ends, 'a' holds the HCF

# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
num1 = int(input("Enter value of A: "))   # Take first number as input
num2 = int(input("Enter value of B: "))   # Take second number as input

ans = hcf(num1, num2)                     # Calculate HCF of num1 and num2
lcm = (num1 * num2) // ans                # Apply formula to get LCM

# ------------------------------------------------------------
# Print the final LCM
# ------------------------------------------------------------
print(lcm)
