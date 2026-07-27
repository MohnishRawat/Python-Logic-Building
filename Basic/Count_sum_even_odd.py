# ------------------------------------------------------------
# Program: Analyze Digits of a Number
# Author: [Your Name]
# Description:
#   This program takes an integer input and performs four analyses:
#     1. Counts total number of digits.
#     2. Calculates the sum of all digits.
#     3. Counts how many digits are even.
#     4. Counts how many digits are odd.
# ------------------------------------------------------------

# ------------------------------------------------------------
# PART 1 — Define helper functions
# ------------------------------------------------------------

def Count(num):
    # Initialize a counter to track digits
    count = 0
    # Loop until the number becomes 0
    while num > 0:
        num //= 10       # Remove the last digit (integer division by 10)
        count += 1       # Increase digit count
    return count         # Return total number of digits


def SUM_of_digits(num):
    # Initialize sum accumulator
    total = 0
    # Loop until the number becomes 0
    while num > 0:
        var = num % 10   # Extract the last digit
        total += var     # Add digit to total sum
        num //= 10       # Remove the last digit
    return total         # Return sum of digits


def Even_Digits(num):
    # Initialize counter for even digits
    count = 0
    while num > 0:
        var = num % 10   # Extract last digit
        if var % 2 == 0: # Check if digit is even
            count += 1   # Increment even counter
        num //= 10       # Remove last digit
    return count         # Return count of even digits


def Odd_Digits(num):
    # Initialize counter for odd digits
    count = 0
    while num > 0:
        var = num % 10   # Extract last digit
        if var % 2 != 0: # Check if digit is odd
            count += 1   # Increment odd counter
        num //= 10       # Remove last digit
    return count         # Return count of odd digits


# ------------------------------------------------------------
# PART 2 — Take input and display results
# ------------------------------------------------------------
num = int(input("Enter a number: "))   # Ask user for input and convert to integer

# Call each function and print results
print("Total Digits : ", Count(num))          # Prints total number of digits
print("Even Digits : ", Even_Digits(num))     # Prints count of even digits
print("Odd Digits : ", Odd_Digits(num))       # Prints count of odd digits
print("Sum of digits : ", SUM_of_digits(num)) # Prints sum of all digits

# ------------------------------------------------------------
# Example Input / Output
# Input:  12345
# Output:
#   Total digits: 5
#   Even digits: 2
#   Odd digits: 3
#   Sum of digits: 15
# ------------------------------------------------------------
