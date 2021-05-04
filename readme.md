# Python Tchat [![CodeFactor](https://www.codefactor.io/repository/github/sigmanificient/pytchat/badge)](https://www.codefactor.io/repository/github/sigmanificient/pytchat)

### A simple texts communication platform using pygame and sockets.

## How to install ?
*You need a python 3.8.6 server with at least one opened port*

- Download the source code from this repo.

### Server
- In your server, copy the `main.py` file from the `server` directory.
- Create a `listen_port` file without any extensions and write which port you want to listen on.
  ```
  port
  ```
    
- run the server using :
  ```
  python -m main.py
  ```

### Client

- On your local computer, open the `main.py` file from the `client` directory.
- Create a file `server` with no extensions and write the address and port of your server like this:
    ```
    server:port
    ```

- If you don't have pygame, you can install via pip. Make sure to follow the requirements for tht package.
  ```
  pip install pygame
  ```
  You can find the package repository here : [pygame repo](https://github.com/pygame/pygame)

 - Run the client ( `main.py` )
