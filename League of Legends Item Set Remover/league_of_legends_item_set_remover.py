import pyautogui
import time

# pyautogui.displayMousePosition()

amount = input('How many item sets to remove?')
print('To remove ' + amount + ' item sets')

def deleteItemSet():
    pyautogui.moveTo(1401, 387)

    time.sleep(0.15)

    pyautogui.click()

    time.sleep(0.15)

    pyautogui.moveTo(1371, 458)

    time.sleep(0.15)

    pyautogui.click()

    time.sleep(0.15)

    pyautogui.moveTo(915, 546)

    time.sleep(0.15)

    pyautogui.click()

for i in range(int(amount)):
    deleteItemSet()
    print(i)
