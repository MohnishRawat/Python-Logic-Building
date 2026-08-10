# ------------------------------------------------------------
# Program: Reverse a Number
# Author: Mohnish Rawat
# Description:
#   This program takes an integer input and reverses its digits.
#   Example: 1234 → 4321
# ------------------------------------------------------------

n = int(input("Enter a number: "))   # Take input from user and convert to integer
rev = 0                              # Initialize variable to store reversed number

# ------------------------------------------------------------
# Loop to reverse digits
# ------------------------------------------------------------
while n > 0:                         # Continue until all digits are processed
    digit = n % 10                   # Extract the last digit
    rev = rev * 10 + digit           # Build reversed number by shifting and adding digit
    n //= 10                         # Remove the last digit from n

# ------------------------------------------------------------
# Print the reversed number
# ------------------------------------------------------------
print("Reversed number:", rev)
