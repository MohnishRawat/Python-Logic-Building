# ------------------------------------------------------------
# Program: Strong Number Checker
# Author: Mohnish Rawat
# Description:
#   A Strong Number is a number in which the sum of the factorials
#   of its digits equals the original number.
#   Example: 145 → 1! + 4! + 5! = 145
# ------------------------------------------------------------


# ------------------------------------------------------------
# Function: fact(t)
# Purpose: Calculate factorial of a digit
# ------------------------------------------------------------
def fact(t):
    if t < 0:  # Factorial is not defined for negative numbers
        return "Factorial is not defined for negative numbers"
    return 1 if t <= 1 else t * fact(t - 1)  # Base case: factorial of 0 or 1 is 1
    # Recursive case: t! = t × (t-1)!


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
n = int(input("Enter a number: "))  # Take input from user
temp = n  # Copy original number into temp
total = 0  # Initialize sum of factorials of digits

# ------------------------------------------------------------
# Loop through each digit of the number
# ------------------------------------------------------------
while temp > 0:
    t = temp % 10  # Extract last digit
    temp //= 10  # Remove last digit
    total += fact(t)  # Add factorial of digit to total sum

# ------------------------------------------------------------
# Final check: Compare sum with original number
# ------------------------------------------------------------
if total == n:  # If sum equals original number
    print("-----Number is STRONG-----")  # Then it's a Strong Number
else:
    print("-----Number is not STRONG-----")  # Otherwise, not Strong
