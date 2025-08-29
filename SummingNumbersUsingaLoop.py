# Ask the user for input
n = int(input("Enter a positive integer: "))

# Initialize the sum
total = 0

# Use a for loop to calculate the sum from 1 to n
for i in range(1, n + 1):
    total += i

# Display the result
print(f"The sum of integers from 1 to {n} is: {total}")