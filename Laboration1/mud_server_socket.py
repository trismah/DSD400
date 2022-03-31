import socket
import time

"""
small_mud.py, Thomas Lundqvist, 2019-2022, use freely!
A small beginning of a MUD, Multi User Dungeon, game.
"""
Current_room = 0
description = [
    "You see a typical class room with a whiteboard in front of you.",
    "You are in a corridor at University West.",
    "You see a restaurant where people eat lunch."]
def parse_and_execute(command):
    global Current_room
    if command == "look" or command == "l":
        return description[Current_room]
    if command == "go east" or command == "e":
        if Current_room < 2:
            Current_room += 1
            return "You walk east!"
        return "You bump into the wall!"
    if command == "go west" or command == "w":
        if Current_room > 0:
            Current_room -= 1
            return "You walk west!"
        return "You bump into the wall!"
    if command == "help" or command == "h" or command == "?":
        return "Try looking around, go east, west, or quit!"
    return "I don't understand your command!"

# Set up socket
HOST = "0.0.0.0"
PORT = 5000

# Make sure the server is listening even if client quits
while True:
    print("Listening...")
    # Using the with statement to always close the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connection with {addr} established.")
            while data := conn.recv(1024).decode():
                conn.send(parse_and_execute(data).encode())
        print(f"Connection to {addr} lost.")
    print("Bye.")
    time.sleep(0.1)
