import errno
import sys
import uuid

HEADER_LENGTH = 10


class Client:

    def __init__(self, client_socket):
        self.name = f"client {uuid.uuid4()}".encode("utf-8")
        self.socket = client_socket

        username_header = f"{len(self.name) : <{HEADER_LENGTH}}".encode("utf-8")
        self.socket.send(username_header + self.name)

        self.send_message = ''

    def send(self):
        message = self.send_message.encode("utf-8")
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode("utf-8")
        self.socket.send(message_header + message)
        self.send_message = ''

    def retrieve_next_message(self, new_messages):
        username_header = self.socket.recv(HEADER_LENGTH)
        if not len(username_header):
            print("Connection closed by the server")
            sys.exit()

        username_length = int(username_header.decode("utf-8").strip())
        username = self.socket.recv(username_length).decode("utf-8")

        message_header = self.socket.recv(HEADER_LENGTH)
        message_length = int(message_header.decode("utf-8").strip())
        message = self.socket.recv(message_length).decode("utf-8")

        new_messages.append({'author': username, 'content': message})

    def fetch_new_messages(self):
        if len(self.send_message):
            self.send()

        new_messages = []

        try:
            while True:
                self.retrieve_next_message(new_messages)

        except IOError as e:
            if e.errno not in [errno.EAGAIN, errno.EWOULDBLOCK]:
                print("reading error", str(e))
                sys.exit()

            return new_messages

        except Exception as e:
            print("general error", str(e))
            sys.exit()
