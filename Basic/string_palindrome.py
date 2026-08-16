# ------------------------------------------------------------
# Program: Palindrome String Checker
# Author: Mohnish Rawat
# Description:
#   A palindrome is a string that reads the same forward and backward.
#   Example: "madam", "racecar", "level"
# ------------------------------------------------------------

ch = input("Enter a string: ")   # Take input string from user

s = 0                            # Start index (first character)
e = len(ch) - 1                  # End index (last character)
flag = True                      # Assume string is palindrome initially

# ------------------------------------------------------------
# Loop to compare characters from both ends
# ------------------------------------------------------------
while s < e:                     # Continue until start crosses end
    if ch[s] != ch[e]:           # If mismatch found
        print("String is not palindrome!")
        flag = False             # Mark as not palindrome
        break                    # Exit loop early
    s += 1                       # Move start index forward
    e -= 1                       # Move end index backward

# ------------------------------------------------------------
# Final check
# ------------------------------------------------------------
if flag:                         # If no mismatch was found
    print("String is palindrome")
