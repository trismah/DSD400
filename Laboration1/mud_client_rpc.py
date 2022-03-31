import xmlrpc.client

HOST = "192.168.8.113"
PORT = 5000

with xmlrpc.client.ServerProxy(f"http://{HOST}:{PORT}") as s:
    print("Welcome to simple MUD, the simple Multi-User Dungeon game.")
    while command := input(': '):
        if command == "quit" or command == "q":
            break
        print(s.parse_and_execute(command))
    
print("Bye.")