import subprocess

ip_address = input("Enter the IP address of the server: ")
port = input("Enter the port you want to connect to: ")

subprocess.run(["nc", "-v", ip_address, port]) # -v is for verbose mode # verbose mode is used to display more information about the connection