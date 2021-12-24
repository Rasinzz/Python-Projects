import time

count = int(input('Enter a number of seconds: '))

while count != 0:
    print(count)
    count -= 1
    time.sleep(1)
else:
    print('Done!')