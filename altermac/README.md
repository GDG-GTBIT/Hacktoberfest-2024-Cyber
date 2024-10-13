# MAC Address Changer

This project is a simple MAC (Media Access Control) address changer for network interfaces, created as part of Hacktoberfest. It generates a random MAC address and applies it to a specific network interface. This project currently supports Linux systems and is open for contributions to add Windows support.

## Features

- Linux Support: Modify MAC addresses on Linux using system-level ioctl calls.
- Random MAC Address Generation: Generates a random, locally administered MAC address.
- Automated Interface Down/Up Handling: Brings down the interface, changes the MAC address, and brings it back up.
- Hacktoberfest Contribution: Open for contributions from the community as part of Hacktoberfest!

## How It Works

The program:

1. Brings down the network interface to prevent any "Device or resource busy" errors.
2. **Generates a random MAC address** (locally administered, unicast).
3. Applies the new MAC address using ioctl to interact with the network interface.
4. Brings the network interface back up, allowing network communication with the new MAC address.

## Requirements

- A Linux system.
- Root privileges (or administrative access) to modify network interfaces.
- GCC compiler.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/GDG-GTBIT/Hacktoberfest-2024-Cyber.git
cd Hacktoberfest-2024-Cyber/altermac
```

2. Build the project using `make`:

```bash
make
```

This will compile the source files into an executable called `altermac`.

## Usage

1. Run the program as root:

```bash
sudo ./altermac <INTERFACE>
```

Replace `<INTERFACE>` with the network interface name, e.g., `eth0` or `wlan0`.

Example:

```bash
sudo ./altermac eth0
```

The program will generate a new random MAC address and apply it to the specified interface.

## Makefile Instructions

Your project includes a `Makefile` to simplify the build process. The following commands are available:

- Build the project:

```bash
make
```

This will compile altermac.c with the optimization flag -O3 and the latest C standard -std=c2x, generating an optimized binary.

- Clean the build:

```bash
    make clean
```
This will remove the compiled binary and object files (`*.o`), cleaning up your working directory.

## Makefile Details

```makefile

opt=-O3 -Wall -std=c2x

all: clean altermac

altermac: altermac.o
	gcc ${opt} $^ -o $@

altermac.o:	altermac.c
	gcc ${opt} -c $^

clean:
	rm -f altermac *.o
```

- The opt variable defines optimization level `-O3`, enables warnings with `-Wall`, and uses the `-std=c2x` standard.
- The target `all` first runs `make clean` and then builds the `altermac` binary.
- The `clean` rule removes the binary and object files.

## Hacktoberfest Contributions

We are actively looking for contributions to improve the project as part of Hacktoberfest! Here’s how you can contribute:

1. Add Windows Support: Modify the program to support Windows by using the Windows Registry and `netsh` commands.
2. Code Improvements: Refactor the code, add more error handling, or improve cross-platform compatibility.
3. Documentation: Enhance the `README.md` or add additional documentation such as man pages.
4. New Features: Feel free to propose new features and improvements!

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request (PR) with your changes.

## Disclaimer

This tool modifies system-level network settings. Please use with caution and ensure that you have appropriate permissions to modify your system’s network configuration. Use at your own risk.
