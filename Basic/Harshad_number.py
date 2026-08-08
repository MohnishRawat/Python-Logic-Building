# ------------------------------------------------------------
# Program: Harshad (Niven) Number Checker
# Author: Mohnish Rawat
# Description:
#   A Harshad number is an integer that is divisible by the sum
#   of its digits.
#   Example: 18 → sum of digits = 9 → 18 % 9 == 0 → Harshad
# ------------------------------------------------------------

n = int(input("Enter a number: "))  # Take input from user and store in variable 'n'
total = 0  # Initialize sum of digits
temp = n  # Copy original number into temp for digit processing

# ------------------------------------------------------------
# Loop to calculate sum of digits
# ------------------------------------------------------------
while temp > 0:  # Continue until all digits are processed
    total += temp % 10  # Extract last digit and add to total
    temp //= 10  # Remove last digit

# ------------------------------------------------------------
# Check Harshad condition
# ------------------------------------------------------------
if n % total == 0:  # If number is divisible by sum of digits
    print("Harshad number")  # Then it's a Harshad number
else:
    print("Not Harshad number")  # Otherwise, not Harshad
