import socket
from threading import Thread

HOST = "localhost"
PORT = 5001

class Client:
    def __init__(self, conn):
        self.conn = conn
        self.messages = []
        self.id = self.get_id()

    def get_id(self):
        return self.conn.recv(1024).decode().strip('\n')

    def send_message(self, message):
        self.conn.send(message.encode())

    def recieve_message(self):
        data = self.conn.recv(1024).decode()
        self.messages.append(data)
        return data

    def _generate_messages(self):
        for message in self.messages:
            yield message

    def return_messages(self):
        return self.messages


def handle_thread(client):
    while  data := client.recieve_message():
        server_messages.append((client.id, f"{data}"))


def print_messages(size):
    while True:
        if size != len(server_messages):
            print(server_messages)
            size = len(server_messages)


def send_messages(server_messages):
    while True:
        if server_messages:
            from_user, message = server_messages.pop()
            for client in clients:                
                if client.id != from_user:
                    client.send_message(f"{from_user}: {message}")

threads = []
clients = []
server_messages = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Starting server.")
    s.bind((HOST, PORT))
    s.listen(10)

    #Thread(target=print_messages, args=(len(server_messages), )).start()
    Thread(target=send_messages, args=(server_messages, )).start()

    while True:
        conn, addr = s.accept()
        print(f"Connected to {addr}.")
        new_client = Client(conn)
        clients.append(new_client)
        threads.append(Thread(target=handle_thread, args=(new_client, )).start())

        




        


