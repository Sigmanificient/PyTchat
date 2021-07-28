from src.core import start
import dotenv

print("Starting Server...")


def main():
    config = dotenv.dotenv_values('.env')

    ip = config.get('ip', '0.0.0.0')
    port = config.get('port')

    if not port:
        print("No port were specified in the configuration.")
        quit()

    start(ip, int(port))


if __name__ == '__main__':
    main()
