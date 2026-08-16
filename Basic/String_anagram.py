# ------------------------------------------------------------
# Program: Anagram Checker
# Author: Mohnish Rawat
# Description:
#   Two strings are anagrams if they contain the same characters
#   with the same frequency, regardless of order.
#   Example: "listen" and "silent" → Anagram
# ------------------------------------------------------------
# ------------------------------------------------------------
# Dry run code
# ------------------------------------------------------------
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
flag = True                          # Assume strings are anagrams initially

# ------------------------------------------------------------
# Check each character of s1 in s2
# ------------------------------------------------------------
for i in s1:
    if i not in s2:                  # If character not found in s2
        print("Not anagram")
        flag = False
        break
    elif i in s2 and s1.count(i) != s2.count(i):  # If frequency mismatch
        print("Not anagram")
        flag = False
        break

# ------------------------------------------------------------
# Final check
# ------------------------------------------------------------
if flag:
    print("String is anagram")




# ------------------------------------------------------------
# Efficient Method
# ------------------------------------------------------------

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("String is anagram")
else:
    print("Not anagram")
