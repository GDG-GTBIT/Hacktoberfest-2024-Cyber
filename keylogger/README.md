
# Keylogger

This keylogger project captures keystrokes and saves them to a log file. It features real-time monitoring of user input and offers a web interface for viewing the logs. This initiative is part of Hacktoberfest. It is designed for both Linux and Windows platforms and invites contributions to expand its capabilities, including the potential implementation of encryption for secure log storage.

## Key Features

- **Real-time Logging**: Captures keystrokes in real time.
- **Web Interface**: View logs through a web interface hosted locally.
- **Lightweight**: Minimal resource usage, designed for efficiency.
- **Cross-Platform**: Compatible with various operating systems.

## How It Works

The keylogger uses the `pynput` library to monitor keyboard events. Keystrokes are logged into a text file, which can be accessed via a simple web interface built with Flask. The web server serves the log file, allowing users to view it in real time.

## Requirements

- Python 3.x
- Flask (`pip install Flask`)
- Pynput (`pip install pynput`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GDG-GTBIT/Hacktoberfest-2024-Cyber.git
   ```
2. Navigate to the repository:
   ```bash
   cd Hacktoberfest-2024-Cyber/keylogger
   ```
3. Install the required libraries (if you haven't already):
   ```bash
   pip install -r requirements.txt
   ```
## Usage

For Windows:
Run the keylogger:
```bash
    python keylogger.py
```
Start the flask server:
```bash
    python app.py
```

For Linux:
Run the keylogger:
```bash
    python3 keylogger.py
```
Start the flask server:
```bash
    python3 app.py
```
## Accessing the Logs:

Open your web browser and navigate to http://localhost:1438/logs to view the captured logs in real time.

Note: The port number used in the application (1438 in this example) is subject to change. Feel free to modify the port number in app.py and when accessing the logs to fit your preferences.


## Hacktoberfest Contribution
We are actively looking for contributions to improve the project! Here’s how you can contribute:

1. Add Encryption: Implement encryption for the log files to enhance security.
2. Code Improvements: Refactor the code, add error handling, or improve cross-platform compatibility.
3. Documentation: Enhance the README.md or add additional documentation.
4. New Features: Feel free to propose new features and improvements!

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request (PR) with your changes.

## Disclaimer

The keylogger can compromise user privacy and security. Using it without consent may lead to unauthorised access to sensitive information and potential legal repercussions. Kindly use it responsibly :)
