# Get input from the user
number = int(input("Enter a number to print its multiplication table: "))

# Print the multiplication table up to 10
print(f"\nMultiplication Table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")