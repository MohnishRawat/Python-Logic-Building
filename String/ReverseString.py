# ------------------------------------------------------------
# Program: Reverse a String
# Author: Mohnish Rawat
# Description:
#   This program demonstrates different ways to reverse a string
#   in Python.
#
#   Features:
#     - Reverse a string using slicing
#     - Reverse a string using a while loop
#     - Display the reversed string using both methods
# ------------------------------------------------------------


# ------------------------------------------------------------
# Step 1: Define the input string
# ------------------------------------------------------------
s = "Mohnish"


# ------------------------------------------------------------
# Step 2: Reverse the string using slicing
# ------------------------------------------------------------
s2 = s[::-1]
print("Reversed string using slicing:", s2)


# ------------------------------------------------------------
# Step 3: Reverse the string using a while loop
#   Start from the last index and keep adding characters
#   to a new string until the first index is reached
# ------------------------------------------------------------
e = len(s) - 1
s1 = ""

while e >= 0:
    s1 += s[e]
    e -= 1


# ------------------------------------------------------------
# Step 4: Display the reversed string
# ------------------------------------------------------------
print("Reversed string using while loop:", s1)
