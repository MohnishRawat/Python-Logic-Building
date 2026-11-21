# ------------------------------------------------------------
# Program: Check Whether a String is a Palindrome
# Author: Mohnish Rawat
# Description:
#   This program checks whether a given string is a palindrome
#   using the two-pointer approach.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 1: Define the input string
# ------------------------------------------------------------
st = "racecar"

# ------------------------------------------------------------
# Step 2: Initialize start and end pointers
# ------------------------------------------------------------
s = 0
e = len(st) - 1
flag = 0

# ------------------------------------------------------------
# Step 3: Compare characters from both ends
# ------------------------------------------------------------
while s < e:
    if st[s] != st[e]:
        flag = 1
        break

    s += 1
    e -= 1

# ------------------------------------------------------------
# Step 4: esult
# ------------------------------------------------------------
if flag == 0:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
