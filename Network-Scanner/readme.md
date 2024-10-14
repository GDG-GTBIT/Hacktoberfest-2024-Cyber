# Network Scanner

A simple network scanner built using Scapy in Python. It provides two types of network scanning capabilities: ARP scanning and TCP SYN scanning.


## Features

- ARP Scan: Discovers devices on the local network by mapping IP addresses to MAC addresses.
- TCP Scan: Scans specified ports using TCP SYN packets to identify open ports

## Requirements
- Python 3.x
- Scapy (pip install scapy)

  
## Usage/Examples

You can perform either an ARP scan or a TCP scan based on the command you provide. For best results, if you're on a UNIX-based system, please run the script with elevated privileges (using sudo).

``` 
usage: scanner.py {ARP,TCP} [-h] [options]

positional arguments:
  {ARP,TCP}   Command to perform (ARP or TCP scan).
    ARP       Perform a network scan using ARP requests.
    TCP       Perform a TCP scan using SYN packets.
```

### ARP Scan
An ARP scan sends ARP requests to devices on the local network and collects ARP replies. You can scan an individual IP or an entire subnet.

### Example

```
python3 scanner.py ARP 192.168.2.1/24

````

This command scans all IP addresses in the 192.168.2.0/24 subnet.

#### Positional Argument:

- IP: A single IP address or a range (e.g., 192.168.1.1/24).

#### Optional Argument:

- -h, --help: Show the help message and exit.

### TCP Scan
A TCP scan sends TCP SYN packets to the specified ports, and identifies open ports by receiving SYN+ACK responses. You can specify individual ports or scan a range of ports.

### Example

```
python3 scanner.py TCP 192.168.2.1 --range 0 1000

````

This command scans all ports from 0 to 1000 on the target 192.168.2.1.

#### Positional Arguments:

- IP: The IP address or hostname of the target.
- ports: Ports to scan (space-separated list).
 
#### Optional Arguments:

- --range: Scans a range of ports. When this option is specified, provide the lower and upper bounds (e.g., 0 1000).
- -h, --help: Show the help message and exit.

## Example Usage

### ARP Scan (Single IP):
```
python3 scanner.py ARP 192.168.1.1
```

### ARP Scan (IP Range):
```
python3 scanner.py ARP 192.168.1.1/24
```

### TCP Scan (Specific Ports):
```
python3 scanner.py TCP 192.168.1.1 22 80 443
```

### TCP Scan (Port Range):

```
python3 scanner.py TCP 192.168.1.1 --range 0 1000
```


# Contributing to Network-Scanner

Thank you for your interest in contributing to the **Network-Scanner** project! We welcome contributions from the community and appreciate your help. Please follow the guidelines below to ensure a smooth contribution process.

## How to Contribute

1. **Fork the Repository:**
   - Click the "Fork" button at the top right of this repository to create a copy of it in your GitHub account.

2. **Clone Your Fork:**
   - Clone the forked repository to your local machine using the following command:
     ```bash
     git clone https://github.com/YOUR_USERNAME/Network-Scanner.git
     ```

3. **Create a Branch:**
   - Create a new branch for your feature or fix:
     ```bash
     git checkout -b feature/my-feature
     ```

4. **Make Your Changes:**
   - Implement your changes or add new features.

5. **Test Your Changes:**
   - Ensure that your modifications work correctly by running any tests and verifying functionality.

6. **Commit Your Changes:**
   - Commit your changes with a descriptive message:
     ```bash
     git add .
     git commit -m "Add feature: Description of changes"
     ```

7. **Push Your Changes:**
   - Push your branch to your forked repository:
     ```bash
     git push origin feature/my-feature
     ```

8. **Create a Pull Request:**
   - Go to the original repository and click on "New Pull Request." Select your branch from the dropdown and submit the pull request for review.
   - Please include a description of your changes and any relevant information.

## Guidelines for Contributions

- **Code Quality:** Please adhere to coding standards and maintain code quality.
- **Documentation:** If you add new features, please update the documentation accordingly.
- **Issue Tracking:** If you're fixing a bug or implementing a feature, please reference the issue in your pull request.

## Reporting Issues

If you encounter bugs or have feature requests, please open an issue in the repository with a detailed description of the problem or suggestion.

## Code of Conduct

By participating in this project, you agree to abide by the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/), which outlines our expectations for participant behavior.

## License

This project is licensed under the MIT License.

Thank you for contributing!