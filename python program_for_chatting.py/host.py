import subprocess

port = input("Enter the port you want to listen on: ")

subprocess.run(["nc", "-lvp", port]) # -l is for listening mode, -v is for verbose mode, -p is for port number  
