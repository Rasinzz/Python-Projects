import random

while True:
    choice = input("Would you like to roll the dice (yes/no)? ")

    if choice == "yes":
        print("Rolled:", random.randint(1, 6))
    elif choice == "no":
        break
    else:
        print("Invalid input (must be 'yes' or 'no')")