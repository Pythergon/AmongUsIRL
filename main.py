#Among us script!
import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT =  'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

class Task:
    def __init__(self, name, location):
        self.isDone = False
        self.name = name
        self.location = location

    def finishTask(self):
        self.isDone = True

    def toString(self):
        print(f"{self.name} - Task is done: ({self.isDone}) - Task location: {self.location}")

class Player:
    def __init__(self, name):
        self.name = name
        self.taskList = []

    def addTaskToList(self, task):
        self.taskList.append(task)

def handle_client(conn, addr):
    #This will handle all server-client communication
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Message Received".encode(FORMAT))
    conn.close()

def start():
    # Server - Server Side ;)
    player1 = Player("Jared")
    task1 = Task("Wires", "Kitchen")
    task1.toString()
    player1.addTaskToList(task1)
    print("Hello, World!")

    # Server - Client Side ;)
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("Server is starting...")
start()

locations = ["Mudroom Bathroom", "Mudroom", "Laundry Room", "Dining Room", "Kitchen"]
