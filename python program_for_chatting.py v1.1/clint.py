import subprocess

# Get IP address and port
ip_address = input("Enter the IP address of the server: ")
port = input("Enter the port you want to connect to: ")

# Validate the port number
if not (port.isdigit() and 1 <= int(port) <= 65535):
    print("Invalid port number. Please enter a number between 1 and 65535.")
else:
    try:
        # Attempt connection using nc
        subprocess.run(["nc", "-v", ip_address, port])
    except Exception as e:
        print(f"An error occurred: {e}")
