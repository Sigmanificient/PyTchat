# Python Tchat

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Sigmanificient/PyTchat/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/Sigmanificient/PyTchat/?branch=main)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Sigmanificient/PyTchat)
![GitHub repo size](https://img.shields.io/github/repo-size/Sigmanificient/PyTchat)
![Lines of code](https://img.shields.io/tokei/lines/github/Sigmanificient/PyTchat)
![GitHub last commit](https://img.shields.io/github/last-commit/Sigmanificient/PyTchat)
![Github](https://shields.io/github/license/Sigmanificient/PyTchat)

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
