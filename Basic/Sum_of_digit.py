# ------------------------------------------------------------
# Program: Sum of Digits
# Author: Mohnish Rawat
# Description:
#   This program calculates the sum of all digits in a given integer.
#   Example: 1234 → 1 + 2 + 3 + 4 = 10
# ------------------------------------------------------------

n = int(input("Enter a number: "))   # Take input from user and convert to integer
total = 0                            # Initialize variable to store sum of digits

# ------------------------------------------------------------
# Loop to extract and add digits
# ------------------------------------------------------------
while n > 0:                         # Continue until all digits are processed
    total += n % 10                  # Extract last digit and add to total
    n //= 10                         # Remove last digit from n

# ------------------------------------------------------------
# Print the final sum of digits
# ------------------------------------------------------------
print(total)                         # Display the sum of digits
