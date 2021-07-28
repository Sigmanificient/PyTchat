# python 3.8.6

import socket
import select
import dotenv

print("Starting Server...")

HEADER_LENGTH = 10
config = dotenv.dotenv_values('.env')

IP = config.get('ip', '0.0.0.0')
port = config.get('port')

if not port:
    print("No port were specified in the configuration.")
    quit()

PORT = int(port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

print("server started")
socket_list = [server_socket]
clients = {}


def receive_message(client_socket_):
    try:
        message_header = client_socket_.recv(HEADER_LENGTH)
        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())
        return {
            "header": message_header,
            "data": client_socket_.recv(message_length)
        }

    except Exception as e:
        print(e)
        return False


while True:
    read_sockets, _, exception_sockets = select.select(
        socket_list, [], socket_list
    )

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)

            if not user:
                continue

            socket_list.append(client_socket)
            clients[client_socket] = user

            print(
                f"Accepted new connection from {client_address[0]}:" 
                f"{client_address[1]} username: {user['data'].decode('utf-8')}"
            )

        else:
            message = receive_message(notified_socket)

            if not message:
                print(
                    "Closed connection from",
                    clients[notified_socket]['data'].decode('utf-8')
                )

                socket_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(
                f"receive_message from {user['data'].decode('utf-8')}:",
                message['data'].decode('utf-8')
            )

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(
                        (
                            user["header"] + user["data"]
                            + message['header'] + message["data"]
                        )
                    )

    for notified_socket in exception_sockets:
        socket_list.remove(notified_socket)
        del clients[notified_socket]
