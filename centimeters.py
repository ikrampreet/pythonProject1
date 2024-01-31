# Ask the fisher for the length of the zander
zander_length = float(input("Enter the length of the zander in centimeters: "))

# Define the size limit
size_limit = 42

# Check if the zander meets the size limit
if zander_length >= size_limit:
    print("Congratulations! The zander meets the size limit.")
else:
    # Calculate how many centimeters below the size limit the fish is
    below_limit = size_limit - zander_length
    print(f"Please release the zander back into the lake. It is {below_limit:.2f} centimeters below the size limit.")