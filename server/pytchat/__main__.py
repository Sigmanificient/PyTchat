import json
import logging
import sys

import dotenv
from websocket_server import WebsocketServer

users = {}


def on_client(client, _srv):
    print(
        '-> Accepted new connection from',
        ':'.join(map(str, client['address'])),
        'connected'
    )


def on_client_left(client, server):
    print('-> Client left:', client['address'])
    username = users.pop(client['address'])
    server.send_message_to_all(
        msg=json.dumps(
            {
                'type': 'logout',
                'username': username
            }
        )
    )


def on_message_received(_client, server, data):
    print('-> Received message from', _client['address'], ':', data)

    data = json.JSONDecoder().decode(data)

    if data['type'] == 'login':
        users[_client['address']] = data['username']
        server.send_message_to_all(
            msg=json.dumps(
                {
                    'type': 'login',
                    'username': data['username']
                }
            )
        )

        server.send_message(
            client=_client,
            msg=json.dumps(
                {
                    'type': 'users',
                    'users': list(users.values())
                }
            )
        )

    elif data['type'] == 'message':
        print(users[_client['address']])
        server.send_message_to_all(
            msg=json.dumps(
                {
                    'type': 'message',
                    'username': users[_client['address']],
                    'message': data['content']
                }
            )
        )


def main():
    port = sys.argv[1] if (len(sys.argv) > 1) else '8080'

    if not port.isdigit():
        print("Port must be a number.")
        return

    server = WebsocketServer(
        host='0.0.0.0',
        port=int(port),
        loglevel=logging.DEBUG
    )

    server.set_fn_new_client(on_client)
    server.set_fn_message_received(on_message_received)
    server.set_fn_client_left(on_client_left)
    server.run_forever()


if __name__ == '__main__':
    main()
