import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"

while True:
    password_length = int(input("How long would you like your password(s) to be?: "))
    password_count = int(input("How many passwords would you like to generate?: "))

    for x in range(0, password_count):
        password = ""

        for x in range(0, password_length):
            password_character = random.choice(characters)
            password += password_character

        print("Here is your password: " + password)