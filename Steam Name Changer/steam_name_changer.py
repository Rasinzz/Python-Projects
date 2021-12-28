from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import tkinter as tk
import time

mouse = MouseController()
keyboard = KeyboardController()

app_width = 500
app_height = 300

root = tk.Tk()

root.title('Steam Name Changer')

# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()

# x = (screen_width / 2) - (app_width / 2)
# y = (screen_height / 2) - (app_height / 2)

x = 1400
y = 700

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

canvas = tk.Canvas(root, width=app_width, height=app_height)
canvas.pack()

frame = tk.Frame(root, bg='#36393F')
frame.place(relwidth=1, relheight=1)

def changeName():
    mouse.position = (467, 53) # Click username
    time.sleep(0.5)
    mouse.position = (453, 102) # Click 'Profile'
    time.sleep(0.5)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = (1185, 283) # Click 'Edit Profile'
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.position = (779, 506) # Click 'Profile Name' textbox
    mouse.click(Button.left, 1)

    # Clear 'Profile Name' textbox
    keyboard.press(Key.ctrl_l)
    keyboard.press('a')
    keyboard.release(Key.ctrl_l)
    keyboard.release('a')
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

    keyboard.type(entry.get())

    time.sleep(0.5)

    mouse.scroll(0, -7)
    time.sleep(0.5)
    mouse.position = (1324, 695)
    mouse.click(Button.left, 1)

entry = tk.Entry(frame, width=20)
entry.place(relx=0.5, rely=0.43, anchor='n')

button = tk.Button(frame, text="Change Name", width=20, command=changeName)
button.place(relx=0.5, rely=0.5, anchor='n')

root.mainloop()
