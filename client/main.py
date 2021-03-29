# python 3.8.6
import random
import socket
import errno
import string
import sys
import time

print("Starting Client...")

HEADER_LENGTH = 16

with open("server") as f:
    IP, PORT = f.read().split(':')
    PORT = int(PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

name = "foo".encode('utf-8')
username_header = f"{len(name) : <{HEADER_LENGTH}}".encode("utf-8")

client_socket.send(username_header + name)

while True:
    message = input(">>> ").encode("utf-8")
    message_header = f"{len(message) :< {HEADER_LENGTH}}".encode("utf-8")
    client_socket.send(message_header + message)

    try:
        username_header = client_socket.recv(HEADER_LENGTH)

        if not len(username_header):
            print("Connection closed by the server")
            sys.exit()

        username_length = int(username_header.decode("utf-8").strip())
        username = client_socket.recv(username_length).decode("utf-8")

        message_header = client_socket.recv(HEADER_LENGTH)
        message_length = int(message_header.decode("utf-8").strip())
        message = client_socket.recv(message_length).decode("utf-8")

        print(username, message)

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print("reading error", str(e))
            sys.exit()

    except Exception as e:
        print("general error", str(e))
        sys.exit()
