from pynput.mouse import Button, Controller as MouseController
import time

mouse = MouseController()

amount = input('How many friends to remove?')
print('To remove ' + amount + ' friends')

def removeFriend():
    mouse.position = (1759, 260) # hover username

    time.sleep(0.5)

    mouse.click(Button.right, 1)

    time.sleep(0.5)

    # mouse.position = (1769, 325) # view career

    # time.sleep(1)

    mouse.position = (1772, 365) # remove friend

    time.sleep(0.5)

    mouse.click(Button.left, 1)

    time.sleep(0.5)

    mouse.position = (797, 625) # confirm

    time.sleep(0.5)

    mouse.click(Button.left, 1)

    time.sleep(0.5)

    mouse.position = (1898, 247) # reset

    time.sleep(0.5)

    mouse.click(Button.left, 1)

time.sleep(3)

for x in range(int(amount)):
    removeFriend()
    print(x)
