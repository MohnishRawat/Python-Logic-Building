# ------------------------------------------------------------
# Program: Palindrome Number Checker
# Author: Mohnish Rawat
# Description:
#   This program checks whether a given integer is a palindrome.
#   A palindrome number reads the same forward and backward.
#   Example: 121, 1331, 12321
# ------------------------------------------------------------

num = int(input("Enter a number: "))   # Take input from user and convert it to integer
temp = num                             # Store the original number in a temporary variable
rev = 0                                # Initialize variable 'rev' to store the reversed number

# ------------------------------------------------------------
# Loop to reverse the digits of the number
# ------------------------------------------------------------
while temp != 0:                       # Continue until all digits are processed
    rev = (rev * 10) + (temp % 10)     # Take last digit of 'temp' and add it to 'rev'
    temp //= 10                        # Remove the last digit from 'temp'

# ------------------------------------------------------------
# Compare reversed number with original number
# ------------------------------------------------------------
if rev == num:                         # If reversed number equals original
    print("---- Number is Palindrome ----")
else:                                  # Otherwise, not a palindrome
    print("---- Number is not Palindrome ----")
