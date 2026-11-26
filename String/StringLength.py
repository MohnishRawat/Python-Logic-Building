# ------------------------------------------------------------
# Program: Find Length of a String
# Author: Mohnish Rawat
# Description:
#   This program demonstrates two ways to find the length
#   of a string:
#
#   Features:
#     - Using built-in len() function
#     - Using a for loop and counter
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 1: Define the input string
# ------------------------------------------------------------
s = "Mohnish"

# ------------------------------------------------------------
# Step 2: Find length using built-in len() function
# ------------------------------------------------------------
print("Length :", len(s))

# ------------------------------------------------------------
# Step 3: Find length manually using a loop
# ------------------------------------------------------------
cnt = 0

for i in s:
    cnt += 1

# ------------------------------------------------------------
# Step 4: Display the length
# ------------------------------------------------------------
print("Length :", cnt)
