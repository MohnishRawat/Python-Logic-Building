# ------------------------------------------
# Program: Check if a 3-digit number is an Armstrong number
# Author: Mohnish Rawat
# Description:
#   An Armstrong number (also called a narcissistic number) is a number
#   that is equal to the sum of the cubes of its digits.
#   Example: 153 → 1³ + 5³ + 3³ = 153
# ------------------------------------------

# Take input from the user
num = int(input("Enter the Number: "))  # Example: 153


# Extract individual digits
a = num % 10  # Extracts the last digit → 3
c = num % 100  # Extracts the last two digits → 53
b = c // 10  # Extracts the middle digit → 5
d = num // 100  # Extracts the first digit → 1

# Check Armstrong condition:
# If the sum of the cubes of each digit equals the original number

if num == (a**3 + b**3 + d**3):
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# ------------------------------------------
# Alternate approach (using loop) – works for any number of digits
# Uncomment below to test a more general version
# ------------------------------------------

"""
n = num  # Store the original number in variable 'n'
temp = n  # Make a copy of 'n' in 'temp' for later use
total = 0  # Initialize total sum of powered digits
count = 0  # Initialize digit counter
arm = 0  # Temporary variable to hold powered digit values

# ------------------------------------------------------------
# First loop: Count how many digits are in the number
# ------------------------------------------------------------
while n > 0:
    count += 1  # Increase digit count by 1
    n //= 10  # Remove the last digit (integer division by 10)

# ------------------------------------------------------------
# Second loop: Calculate the Armstrong sum
# ------------------------------------------------------------
while temp > 0:
    arm = (temp % 10) ** count  # Take last digit, raise it to 'count' power
    temp //= 10  # Remove the last digit
    total += arm  # Add powered digit to total sum

# ------------------------------------------------------------
# Final check: Compare original number with Armstrong sum
# ------------------------------------------------------------
if num == total:
    print("Armstrong number")  # If equal → Armstrong number
else:
    print("Not an Armstrong number")  # Otherwise → Not Armstrong

"""
