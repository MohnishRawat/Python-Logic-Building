# ------------------------------------------------------------
# Program: Count Frequency of Characters in a String
# Author: Mohnish Rawat
# Description:
#   This program counts the occurrence of each character
#   present in a given string.
#
#   Features:
#     - Uses a dictionary for frequency counting
#     - Displays frequency of every character
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 1: Define the input string
# ------------------------------------------------------------
s = "google.com"

# ------------------------------------------------------------
# Step 2: Create an empty dictionary
# ------------------------------------------------------------
freq = {}

# ------------------------------------------------------------
# Step 3: Count frequency of each character
# ------------------------------------------------------------
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# ------------------------------------------------------------
# Step 4: Display character frequencies
# ------------------------------------------------------------
print(freq)
