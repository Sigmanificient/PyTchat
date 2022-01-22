import logging

import dotenv
from websocket_server import WebsocketServer


def on_client(client, _srv):
    print(
        '-> Accepted new connection from',
        ':'.join(map(str, client['address'])),
        'connected'
    )


def on_message_received(_client, server, message):
    print('-> Received message from', _client['address'], ':', message)
    server.send_message_to_all(message)


def main():
    config = dotenv.dotenv_values('.env')
    port = config.get('port')

    if not port:
        print("No port were specified in the configuration.")
        return

    if not port.isdigit():
        print("Port must be a number.")
        return

    server = WebsocketServer(
        host=config.get('ip', '0.0.0.0'),
        port=int(port),
        loglevel=logging.DEBUG
    )

    server.set_fn_new_client(on_client)
    server.set_fn_message_received(on_message_received)
    server.run_forever()


if __name__ == '__main__':
    main()
