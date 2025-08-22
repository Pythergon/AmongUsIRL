import socket

HEADER = 64
PORT = 5050
FORMAT =  'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.1.10.60"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    #Why wont this work mate :(
    #print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send(DISCONNECT_MESSAGE)

send("Test!")

