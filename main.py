import time
from threading import Thread
from pynput import mouse, keyboard

clicks_per_second = 50

clicking = False

mouse_controller = mouse.Controller()


def click_mouse():
    while True:
        if clicking:
            mouse_controller.click(mouse.Button.left)
            time.sleep(1 / clicks_per_second)


def on_press(key):
    global clicking
    try:
        if key.char == 'p':
            clicking = True
    except AttributeError:
        pass


def on_release(key):
    global clicking
    try:
        if key.char == 'p':
            clicking = False
    except AttributeError:
        pass


# Start the mouse clicking thread
click_thread = Thread(target=click_mouse)
click_thread.daemon = True
click_thread.start()

# Create a keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
