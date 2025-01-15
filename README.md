
---

# Network Communication Scripts

Welcome to the **Network Communication Scripts**, a simple yet powerful Python-based solution to facilitate basic client-server communication using `nc` (Netcat). This repository contains two scripts: one to host a server that listens on a specified port (`host.py`) and another to connect to that server (`client.py`). Both scripts offer basic functionality for testing network connectivity and port listening.

## Overview

- **host.py**: This script listens on a given port and waits for incoming connections. It's perfect for creating a simple server for testing purposes.
- **client.py**: This script connects to the server using the provided IP address and port. It helps verify connectivity and test basic client-server communication.

Both scripts use the `nc` (Netcat) tool to establish communication and verify connections.

## Requirements

- **Python 3.x**
- **Netcat** (`nc`): A powerful networking tool to listen for connections and send data. It should be installed on your system (usually available via `apt`, `yum`, or `brew`).

If `nc` is not installed on your system, you can install it with the following commands:

```bash
# On Ubuntu/Debian:
sudo apt install netcat

# On macOS:
brew install netcat
```

## Usage

### 1. Hosting the Server (`host.py`)

To start a server, run `host.py`, and specify the port you want it to listen on. This will allow the server to accept incoming connections on that port.

```bash
python3 host.py
```

You will be prompted to enter a port number, and the script will validate that it’s within the acceptable range (1-65535). Once validated, it will start listening for incoming connections.

### Example Output:

```
Enter the port you want to listen on: 12345
```

The script will now listen on port `12345` and wait for a connection from a client.

### 2. Connecting as a Client (`client.py`)

To connect to the server, run `client.py`, providing the server's IP address and port.

```bash
python3 client.py
```

You will be prompted to enter the IP address and port number. If the server is running on the specified IP and port, the connection will be established.

### Example Output:

```
Enter the IP address of the server: 192.168.1.1
Enter the port you want to connect to: 12345
```

The client will try to establish a connection to the given IP and port using `nc`.

## Code Walkthrough

### `host.py`

- **User Input**: The script asks the user for a port to listen on.
- **Port Validation**: Ensures the entered port number is valid (between 1 and 65535).
- **Listening for Connections**: Uses `subprocess.run()` to invoke `nc` in listen mode (`-lvp`) on the specified port.

### `client.py`

- **User Input**: The script asks for the server's IP address and port.
- **Port Validation**: Ensures the entered port number is valid.
- **Connection Attempt**: Uses `subprocess.run()` to invoke `nc` in verbose mode (`-v`) to attempt a connection to the specified IP and port.

## Error Handling

Both scripts feature basic error handling:
- **Invalid Port Input**: The script checks if the port is within the valid range (1-65535).
- **Connection Errors**: If the client fails to connect, it will print an error message indicating the issue.

## Example Use Case

1. Start `host.py` on a server or machine, listening on port `12345`.
2. From a different machine, run `client.py` and connect to the server's IP and port (`12345`).
3. The client will attempt to connect to the server, and if successful, communication can occur over that port.

## Contributing

Feel free to fork, clone, or contribute to this repository! If you find bugs or want to suggest improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
