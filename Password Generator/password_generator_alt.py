import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*()"

all = lower + upper + number + symbol
length = int(input('Enter password length: '))
password = "".join(random.sample(all, length))

print('Password: ' + password)