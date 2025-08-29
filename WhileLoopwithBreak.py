while True:
    number = float(input("Enter a number greater than 10: "))

    if number > 10:
        print("Thank you! You entered a number greater than 10.")
        break
    else:
        print("That number is not greater than 10. Try again.\n")
