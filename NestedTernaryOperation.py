# Take input from the user
number = float(input("Enter a number: "))

# Use nested ternary operation to check the sign
result = "Positive" if number > 0 else ("Negative" if number < 0 else "Zero")

# Print the result
print(result)