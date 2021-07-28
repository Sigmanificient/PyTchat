import dotenv
import socket

from src.client import Client
from src.ui import App


def main():
    print("Starting Client...")

    config = dotenv.dotenv_values('.env')

    ip = config.get('ip')
    if not ip:
        print("No server address were specified.")
        return

    port = config.get('port')
    if not port:
        print("No server port were specified.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((ip, int(port)))
    client_socket.setblocking(False)

    app = App(Client(client_socket))
    app.run()


if __name__ == '__main__':
    main()
