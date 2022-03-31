import socket

HOST = "192.168.8.113"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    print("Welcome to simple MUD, the simple Multi-User Dungeon game.")
    while command := input(': '):
        if command == "quit" or command == "q":
            break
        s.send(command.encode())
        data = s.recv(1024)
        print(data.decode())
    
print("Bye.")
