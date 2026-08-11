# ------------------------------------------------------------
# Program: Count Digits in a Number
# Author: Mohnish Rawat
# Description:
#   This program counts how many digits are present in a given integer.
#   Example: 12345 → 5 digits
# ------------------------------------------------------------

n = int(input("Enter a number: "))   # Take input from user and convert to integer
total = 0                            # Initialize counter for digits

# ------------------------------------------------------------
# Loop to count digits
# ------------------------------------------------------------
while n > 0:                         # Continue until all digits are processed
    total += 1                       # Increase digit count by 1
    n //= 10                         # Remove the last digit from n

# ------------------------------------------------------------
# Print the total number of digits
# ------------------------------------------------------------
print(total)                         # Display the count of digits
