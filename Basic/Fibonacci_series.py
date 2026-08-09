# ------------------------------------------------------------
# Program: Fibonacci Number Generator
# Author: Mohnish Rawat
# Description:
#   This program calculates the nth Fibonacci number.
#   The Fibonacci sequence starts with 0, 1 and each next term
#   is the sum of the previous two terms.
#   Example: 0, 1, 1, 2, 3, 5, 8, 13...
# ------------------------------------------------------------

n = int(input("Enter a number: "))   # Take input from user (nth term to generate)

a, b = 0, 1                          # Initialize first two Fibonacci numbers: a=0, b=1

# ------------------------------------------------------------
# Loop to calculate Fibonacci sequence up to nth term
# ------------------------------------------------------------
for i in range(0, n):                # Repeat n times
    a, b = b, a + b                  # Update values: new a = old b, new b = old a+old b

# ------------------------------------------------------------
# Print the nth Fibonacci number
# ------------------------------------------------------------
print(a)                             # After loop, 'a' holds the nth Fibonacci number
