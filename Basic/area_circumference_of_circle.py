# ------------------------------------------------------------
# Program: Area and Circumference of a Circle
# Author: Mohnish Rawat
# Description:
#   This program calculates the area and circumference of a circle
#   given its radius.
#   Formula:
#     Area = π × r²
#     Circumference = 2 × π × r
#   Example: radius = 7 → Area = 153.86, Circumference = 43.96
# ------------------------------------------------------------

PI = 3.14                                # Approximate value of π (pi)
radius = int(input("Enter the radius of the circle: "))   # Take radius as input

area = PI * (radius**2)                  # Calculate area using formula πr²
circumference = 2 * PI * radius          # Calculate circumference using formula 2πr

# ------------------------------------------------------------
# Print the results
# ------------------------------------------------------------
print("Area of Circle: ", area)          # Display area
print("Circumference of Circle: ", circumference)  # Display circumference
