# ------------------------------------------------------------
# Program: Display First Two and Last Two Characters
# Author: Mohnish Rawat
# Description:
#   This program prints a new string made of the first
#   two and last two characters of a string.
#
#   Features:
#     - Handles strings with length less than 2
#     - Uses string slicing
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 1: Define the input string
# ------------------------------------------------------------
s = "w3resource"

# ------------------------------------------------------------
# Step 2: Check string length
# ------------------------------------------------------------
if len(s) < 2:
    print("")
else:

    # --------------------------------------------------------
    # Step 3: Extract first two and last two characters
    # --------------------------------------------------------
    st = s[0:2] + s[len(s)-2:len(s)]

    # --------------------------------------------------------
    # Step 4: Display the result
    # --------------------------------------------------------
    print(st)
