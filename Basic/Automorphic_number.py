# ------------------------------------------------------------
# Program: Automorphic Number Checker
# Author: Mohnish Rawat
# Description:
#   An Automorphic number is a number whose square ends with
#   the same digits as the number itself.
#   Example: 25 → 25² = 625 → ends with 25 → Automorphic
# ------------------------------------------------------------

n = int(input("Enter a Number: "))   # Take input from user and convert to integer

t = n**2                             # Calculate square of the number

mod = 10 ** len(str(n))              # Find modulus value based on number of digits
                                     # Example: if n has 2 digits → mod = 100

temp = t % mod                       # Extract last 'len(str(n))' digits of the square

# ------------------------------------------------------------
# Compare extracted digits with original number
# ------------------------------------------------------------
if temp == n:                        # If last digits match the number
    print("Automorphic number")      # Then it's Automorphic
else:
    print("Not Automorphic number")  # Otherwise, not Automorphic
