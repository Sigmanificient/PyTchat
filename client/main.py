import errno
import socket
import sys
import uuid

import dotenv

HEADER_LENGTH = 10

print("Starting Client...")

config = dotenv.dotenv_values('.env')

IP = config.get('ip')
if not IP:
    print("No server address were specified.")
    quit()

PORT = config.get('port')
if not PORT:
    print("No server port were specified.")
    quit()


class Client:

    def __init__(self):
        self.name = f"client {uuid.uuid4()}".encode("utf-8")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((IP, PORT))
        self.socket.setblocking(False)

        username_header = f"{len(self.name) : <{HEADER_LENGTH}}".encode("utf-8")
        self.socket.send(username_header + self.name)

        self.send_message = ''

    def fetch_new_messages(self):
        if len(self.send_message):
            message = self.send_message.encode("utf-8")
            message_header = f"{len(message) :< {HEADER_LENGTH}}".encode("utf-8")
            self.socket.send(message_header + message)
            self.send_message = ''

        new_messages = []

        try:
            while True:
                username_header = self.socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    print("Connection closed by the server")
                    sys.exit()

                username_length = int(username_header.decode("utf-8").strip())
                username = self.socket.recv(username_length).decode("utf-8")

                message_header = self.socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode("utf-8").strip())
                message = self.socket.recv(message_length).decode("utf-8")

                new_messages.append({
                    'author': username,
                    'content': message
                })

        except IOError as e:
            if e.errno not in [errno.EAGAIN, errno.EWOULDBLOCK]:
                print("reading error", str(e))
                sys.exit()

            return new_messages

        except Exception as e:
            print("general error", str(e))
            sys.exit()
