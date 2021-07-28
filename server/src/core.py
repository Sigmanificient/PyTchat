import select
import socket

HEADER_LENGTH = 10


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


def start(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((ip, port))
    server_socket.listen()

    print("server started")
    socket_list = [server_socket]
    clients = {}

    while True:
        run_cycle(server_socket, socket_list, clients)


def register_user_connection(server_socket, socket_list, clients):
    client_socket, client_address = server_socket.accept()

    user = receive_message(client_socket)

    if not user:
        return

    socket_list.append(client_socket)
    clients[client_socket] = user

    print(
        f"Accepted new connection from {client_address[0]}:"
        f"{client_address[1]} username: {user['data'].decode('utf-8')}"
    )


def remove_user_connection(clients, notified_socket, socket_list):
    print(
        "Closed connection from",
        clients[notified_socket]['data'].decode('utf-8')
    )

    socket_list.remove(notified_socket)
    clients.pop(notified_socket)
    return


def send_message_to(client_socket, user, message):
    client_socket.send(
        user["header"] + user["data"] + message['header'] + message["data"]
    )


def broadcast_message(clients, notified_socket, user, message):
    for client_socket in clients:
        if client_socket != notified_socket:
            send_message_to(client_socket, user, message)


def handle_message(clients, notified_socket, message):
    user = clients[notified_socket]
    print(
        f"receive_message from {user['data'].decode('utf-8')}:",
        message['data'].decode('utf-8')
    )

    broadcast_message(clients, notified_socket, user, message)


def handle_notified_socket(clients, notified_socket, socket_list):
    message = receive_message(notified_socket)

    if not message:
        remove_user_connection(clients, notified_socket, socket_list)
        return

    handle_message(clients, notified_socket, message)


def run_cycle(server_socket, socket_list, clients):
    read_sockets, _, exception_sockets = select.select(
        socket_list, [], socket_list
    )

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            register_user_connection(server_socket, socket_list, clients)

        else:
            handle_notified_socket(clients, notified_socket, socket_list)

    for notified_socket in exception_sockets:
        socket_list.remove(notified_socket)
        clients.pop(notified_socket)
