# PyKeylogger

**Description:** PyKeylogger is a simple keylogging application built with Python. It captures keystrokes on a target machine and stores them in an encrypted log file. This project is intended for educational purposes only, such as understanding how keyloggers work and their implications in cybersecurity.

## Features
- **Keylogging:** Captures keystrokes along with timestamps.
- **Encryption:** Encrypts log data for secure storage using the cryptography library.
- **Remote Control:** Start and stop the keylogger via a web interface built with Flask.
- **User-Friendly Log Viewing:** View decrypted logs in a structured format through a simple API.

## Requirements
- **Python Version:** Python 3.x
- **Libraries:**
    - `pynput`: for keyboard listening
    - `Flask`: for creating the web server
    - `cryptography`: for encryption

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/PyKeylogger.git
   cd PyKeylogger
   ```

2. **Install the required packages**
   ```bash
   pip install pynput Flask cryptography
   ```

3. **Generate an encryption key**
   ```bash
   python -c "from encryptor import Encryptor; Encryptor.generate_key()"
   ```

4. **Start the command server**
   ```bash
   python command_server.py
   ```

## Usage
- **Start Keylogger:** Start the keylogger using Postman or curl.
   ```bash
   curl -X POST http://localhost:5000/start
   ```

- **Stop Keylogger:** Stop the keylogger.
   ```bash
   curl -X POST http://localhost:5000/stop
   ```

- **View Logs:** View the logs.
   ```bash
   curl -X GET http://localhost:5000/view-log
   ```

- **Example Log Response:**
   ```json
   {
       "log": [
           {"timestamp": "2024-11-01 12:00:00", "key": "a"},
           {"timestamp": "2024-11-01 12:00:01", "key": "b"},
           {"timestamp": "2024-11-01 12:00:02", "key": "c"}
       ]
   }
   ```

## Ethical Considerations
This project is intended for ethical hacking and educational purposes. Always ensure you have explicit permission from the target user before deploying keylogging software. Unauthorized use of keyloggers can lead to legal consequences.

## Possible Applications
- **Educational Purposes:** Learn about keyloggers and their functionality in cybersecurity.
- **Cybersecurity Research:** Study keylogging methods to understand and defend against them.
- **Consent-Based Monitoring:** Implement for monitoring your own devices with permission.

## Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer
The author of this project takes no responsibility for the misuse of the code or any actions taken using this software. Use it at your own risk and ensure compliance with local laws and regulations.

## Note
If you're interested in learning more about ethical hacking and cybersecurity practices, consider exploring additional resources or training programs that focus on legal and responsible use of security tools.
