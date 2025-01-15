import subprocess

port = input("Enter the port you want to listen on: ")

# Validate the port number
if port.isdigit() and 1 <= int(port) <= 65535:
    subprocess.run(["nc", "-lvp", port])
else:
    print("Invalid port number. Please enter a number between 1 and 65535.")
