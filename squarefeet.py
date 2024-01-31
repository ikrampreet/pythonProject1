# Conversion factor: 1 square meter = 10.764 square feet
CONVERSION_FACTOR = 10.764

# Prompt user for input
area_in_square_meters = float(input("Enter the area of the house in square meters: "))

# Convert square meters to square feet
area_in_square_feet = area_in_square_meters * CONVERSION_FACTOR

# Display the result
print(f"The area of the house is {area_in_square_feet:.2f} square feet.")