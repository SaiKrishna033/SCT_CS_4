---

# Basic Keylogger

This is a simple keylogger program that records and logs keystrokes. The program captures keyboard events and saves them to a file. It is intended for educational purposes only.

## Features

- Logs all keystrokes.
- Saves keystrokes to a specified log file.
- Stops logging when the `Esc` key is pressed.

## Prerequisites

- Python 3.x
- `pynput` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/SaiKrishna033/basic-keylogger.git
    cd basic-keylogger
    ```

2. Install the required library:

    ```sh
    pip install pynput
    ```

## Usage

1. Run the keylogger script:

    ```sh
    python keylogger.py
    ```

2. The script will start logging keystrokes and save them to `key_log.txt` in the same directory.

3. To stop the keylogger, press the `Esc` key.

## Example Output

The logged keystrokes will be saved in `key_log.txt` and will look like this:

```
h e l l o   w o r l d !  <Key.space>  <Key.backspace>  <Key.enter>
```

## Disclaimer

This keylogger is intended for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Always obtain proper consent before using this tool.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

---
