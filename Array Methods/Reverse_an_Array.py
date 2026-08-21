# ------------------------------------------------------------
# Program: Reverse an Array
# Author: Mohnish Rawat
# Description:
#   This program accepts 'n' numbers from the user, stores them in
#   an array, and then reverses the array using two-pointer logic.
#   Example: arr = [1, 5, 4, 2, 3] → reversed = [3, 2, 4, 5, 1]
# ------------------------------------------------------------

n = int(input("Enter the size of the array: "))   # Step 1: Take input for array size
arr = list()                                      # Step 2: Initialize empty list to store elements

for i in range(0, n):                             # Step 3: Loop 'n' times to accept elements
    x = int(input("Enter the element: "))         # Step 4: Read each element from user
    arr.append(x)                                 # Step 5: Add element to the array
print(arr)                                        # Step 6: Print original array

s, e = 0, n - 1                                   # Step 7: Initialize two pointers (start & end)

while s < e:                                      # Step 8: Loop until start crosses end
    temp = arr[s]                                 # Step 9: Store start element in temp
    arr[s] = arr[e]                               # Step 10: Replace start element with end element
    arr[e] = temp                                 # Step 11: Replace end element with temp (swap done)
    s += 1                                        # Step 12: Move start pointer forward
    e -= 1                                        # Step 13: Move end pointer backward

print(arr)                                        # Step 14: Print reversed array
