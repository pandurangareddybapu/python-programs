# Print even numbers between 1 and 20 using continue
for number in range(1, 21):
    if number % 2 != 0:
        continue  # Skip odd numbers
    print(number)