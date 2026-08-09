# ------------------------------------------------------------
# Program: Factorial of a Number
# Author: Mohnish Rawat
# Description:
#   This program calculates the factorial of a given number
#   using two approaches:
#     1. Recursive function
#     2. Iterative loop
#   Factorial definition:
#     n! = n × (n-1) × (n-2) × ... × 1
#   Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
# ------------------------------------------------------------


# ------------------------------------------------------------
# Recursive Function to calculate factorial
# ------------------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:  # Recursive case: n! = n × (n-1)!
        return n * factorial(n - 1)


# ------------------------------------------------------------
# Main Program
# ------------------------------------------------------------
n = int(input("Enter a number: "))  # Take input from user

fact = 1  # Initialize variable for iterative factorial

# ------------------------------------------------------------
# Iterative loop to calculate factorial
# ------------------------------------------------------------
for i in range(1, n + 1):  # Loop from 1 to n
    fact *= i  # Multiply fact by i each time

# ------------------------------------------------------------
# Print results from both methods
# ------------------------------------------------------------
print(fact)  # Print factorial calculated by iteration
print(factorial(n))  # Print factorial calculated by recursion
