# ------------------------------------------------------------
# Program: Find Maximum and Minimum in Array
# Author: Mohnish Rawat
# Description:
#   This program finds the largest and smallest number in a list.
#   Example: arr = [1, 5, 4, 2, 3] → max=5, min=1
# ------------------------------------------------------------

arr = [1, 5, 4, 2, 3]               # Define array

mx = -(2**63)                       # Initialize max with very small number
mn = (2**63) - 1                    # Initialize min with very large number

# ------------------------------------------------------------
# Loop through array elements
# ------------------------------------------------------------
for i in range(0, len(arr)):
    if arr[i] > mx:                 # If current element is greater than max
        mx = arr[i]                 # Update max
    if arr[i] < mn:                 # If current element is smaller than min
        mn = arr[i]                 # Update min

# ------------------------------------------------------------
# Print results
# ------------------------------------------------------------
print(mx)                           # Largest element
print(mn)                           # Smallest element
